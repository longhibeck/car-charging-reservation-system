import os

import httpx
from fastapi import APIRouter, Depends, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from database import get_db
from models.user import User
from utils import create_token

LOGIN_URL = "https://dummyjson.com/auth/login"

router = APIRouter()
templates_dir = os.path.join(os.path.dirname(__file__), "..", "templates")
templates = Jinja2Templates(directory=templates_dir)


@router.get("/login", response_class=HTMLResponse)
def login_form(request: Request, next: str = None):
    # Store the original URL in session if provided
    if next:
        request.session["next_url"] = next

    return templates.TemplateResponse("login.html", {"request": request})


@router.post("/login", response_class=HTMLResponse)
async def login(
    request: Request,
    username: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db),
):
    try:
        # Authenticate with DummyJSON
        async with httpx.AsyncClient(verify=False) as client:
            response = await client.post(
                LOGIN_URL, json={"username": username, "password": password}
            )

        if response.status_code == 200:
            data = response.json()
            external_user_id = data.get("id")
            current_username = data.get("username")

            if not external_user_id:
                return templates.TemplateResponse(
                    "login.html",
                    {
                        "request": request,
                        "error": "Invalid response from login service",
                    },
                )

            existing_user = (
                db.query(User).filter(User.external_user_id == external_user_id).first()
            )

            if not existing_user:
                new_user = User(
                    external_user_id=external_user_id, username=current_username
                )
                db.add(new_user)
                db.commit()
                db.refresh(new_user)
                print(
                    f"Created new user: {current_username} (external_id: {external_user_id})"
                )
            else:
                if existing_user.username != current_username:
                    old_username = existing_user.username
                    existing_user.username = current_username
                    db.commit()
                    print(
                        f"Updated username for user {external_user_id}: {old_username} -> {current_username}"
                    )

            token = create_token(str(external_user_id))

            request.session.update(
                {
                    "token": token,
                    "username": current_username,
                    "external_user_id": external_user_id,
                }
            )

            next_url = request.session.pop("next_url", "/")
            return RedirectResponse(url=next_url, status_code=302)
        else:
            error_msg = "Invalid credentials"
            try:
                error_data = response.json()
                error_msg = error_data.get("message", error_msg)
            except:
                pass

            return templates.TemplateResponse(
                "login.html", {"request": request, "error": error_msg}
            )

    except httpx.RequestError as e:
        print(f"Request error: {e}")
        return templates.TemplateResponse(
            "login.html",
            {"request": request, "error": "Unable to connect to login service"},
        )
    except Exception as e:
        print(f"Login error: {e}")
        return templates.TemplateResponse(
            "login.html", {"request": request, "error": "Login failed"}
        )


@router.get("/logout")
def logout(request: Request):
    request.session.clear()
    return RedirectResponse(url="/login", status_code=302)
