from fastapi import FastAPI, Depends, Request, Form
from sqlalchemy.orm import Session
from fastapi.responses import RedirectResponse
from starlette.templating import Jinja2Templates

from database import SessionLocal, init_db
import crud

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Initialisation de la base de données
init_db()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root(request: Request, db: Session = Depends(get_db)):
    users = crud.get_users(db)
    return templates.TemplateResponse("index.html", {"request": request, "users": users, "user": None})

@app.post("/add/")
def add_user(name: str = Form(...), email: str = Form(...), db: Session = Depends(get_db)):
    crud.create_user(db, name, email)
    return RedirectResponse(url="/", status_code=303)

@app.get("/edit/{user_id}")
def edit_user_form(user_id: int, request: Request, db: Session = Depends(get_db)):
    users = crud.get_users(db)
    user = crud.get_user(db, user_id)
    return templates.TemplateResponse("index.html", {"request": request, "users": users, "user": user})

@app.post("/edit/{user_id}")
def edit_user(user_id: int, name: str = Form(...), email: str = Form(...), db: Session = Depends(get_db)):
    crud.update_user(db, user_id, name, email)
    return RedirectResponse(url="/", status_code=303)

@app.get("/delete/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    crud.delete_user(db, user_id)
    return RedirectResponse(url="/", status_code=303)
