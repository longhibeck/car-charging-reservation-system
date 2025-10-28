import os

from fastapi import APIRouter, Depends, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from database import get_db
from models.car import Car, Connector, ConnectorType
from models.user import User

router = APIRouter()
templates_dir = os.path.join(os.path.dirname(__file__), "..", "templates")
templates = Jinja2Templates(directory=templates_dir)


@router.get("/car", response_class=HTMLResponse)
def cars_page(request: Request, db: Session = Depends(get_db)):
    if "token" not in request.session:
        return RedirectResponse(url="/login", status_code=302)

    username = request.session.get("username", "User")
    external_user_id = request.session.get("external_user_id")
    if not external_user_id:
        return RedirectResponse(url="/login", status_code=302)

    user = db.query(User).filter(User.external_user_id == external_user_id).first()
    cars = user.cars if user else []

    return templates.TemplateResponse(
        "car.html",
        {
            "request": request,
            "username": username,
            "cars": cars,
            "connector_types": list(ConnectorType),
        },
    )


@router.get("/car/add", response_class=HTMLResponse)
def add_car_form(request: Request):
    if "token" not in request.session:
        return RedirectResponse(url="/login", status_code=302)
    username = request.session.get("username", "User")
    return templates.TemplateResponse(
        "car_add.html",
        {
            "request": request,
            "username": username,
            "connector_types": list(ConnectorType),
        },
    )


@router.post("/car/add", response_class=HTMLResponse)
def add_car(
    request: Request,
    name: str = Form(...),
    connector_types: list[str] = Form(...),
    battery_charge_limit: int = Form(80),
    battery_size: int = Form(50),
    max_kw_ac: int = Form(11),
    max_kw_dc: int = Form(50),
    db: Session = Depends(get_db),
):
    if "token" not in request.session:
        return RedirectResponse(url="/login", status_code=302)

    external_user_id = request.session.get("external_user_id")
    if not external_user_id:
        return RedirectResponse(url="/login", status_code=302)

    user = db.query(User).filter(User.external_user_id == external_user_id).first()
    if not user:
        return RedirectResponse(url="/login", status_code=302)

    new_car = Car(
        name=name,
        battery_charge_limit=battery_charge_limit,
        battery_size=battery_size,
        max_kw_ac=max_kw_ac,
        max_kw_dc=max_kw_dc,
        user_id=user.id,
    )
    db.add(new_car)
    db.flush()

    for ctype in connector_types:
        connector = Connector(
            type=ConnectorType[ctype],
            car_id=new_car.id,
        )
        db.add(connector)
    db.commit()

    return RedirectResponse(url="/car", status_code=302)
