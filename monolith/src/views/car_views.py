import os

from fastapi import APIRouter, Depends, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from database import get_db
from models.car import Car
from models.user import User

router = APIRouter()
templates_dir = os.path.join(os.path.dirname(__file__), "..", "templates")
templates = Jinja2Templates(directory=templates_dir)


@router.get("/car", response_class=HTMLResponse)
def cars_page(request: Request, db: Session = Depends(get_db)):
    if "token" not in request.session:
        return RedirectResponse(url="/login", status_code=302)

    username = request.session.get("username", "User")
    external_user_id = request.session.get("external_user_id")  # Get this from session

    if not external_user_id:
        return RedirectResponse(url="/login", status_code=302)

    # Find user by external_user_id (stable identifier)
    user = db.query(User).filter(User.external_user_id == external_user_id).first()

    if user:
        cars = user.cars
    else:
        cars = []

    return templates.TemplateResponse(
        "car.html", {"request": request, "username": username, "cars": cars}
    )


@router.post("/car/add", response_class=HTMLResponse)
def add_car(
    request: Request,
    license_plate: str = Form(...),
    model: str = Form(...),
    db: Session = Depends(get_db),
):
    if "token" not in request.session:
        return RedirectResponse(url="/login", status_code=302)

    username = request.session.get("username")
    external_user_id = request.session.get("external_user_id")

    if not external_user_id:
        return RedirectResponse(url="/login", status_code=302)

    # Find user by external_user_id
    user = db.query(User).filter(User.external_user_id == external_user_id).first()

    if not user:
        return RedirectResponse(url="/login", status_code=302)

    # Check if license plate already exists
    existing_car = db.query(Car).filter(Car.license_plate == license_plate).first()
    if existing_car:
        cars = user.cars
        return templates.TemplateResponse(
            "car.html",
            {
                "request": request,
                "username": username,
                "cars": cars,
                "error": f"License plate {license_plate} already exists!",
            },
        )

    # Create new Car and link to user
    new_car = Car(
        license_plate=license_plate,
        model=model,
        user_id=user.id,  # Use the internal database ID
    )

    db.add(new_car)
    db.commit()
    db.refresh(new_car)

    return RedirectResponse(url="/car", status_code=302)
