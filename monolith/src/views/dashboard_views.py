import os

from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from database import get_db
from models.user import User

router = APIRouter()
templates_dir = os.path.join(os.path.dirname(__file__), "..", "templates")
templates = Jinja2Templates(directory=templates_dir)


@router.get("/", response_class=HTMLResponse)
def dashboard(request: Request, db: Session = Depends(get_db)):
    if "token" not in request.session:
        return RedirectResponse(url="/login", status_code=302)
    username = request.session.get("username", "User")
    external_user_id = request.session.get("external_user_id")
    user = db.query(User).filter(User.external_user_id == external_user_id).first()
    cars = user.cars if user else []
    return templates.TemplateResponse(
        "dashboard.html", {"request": request, "username": username, "cars": cars}
    )
