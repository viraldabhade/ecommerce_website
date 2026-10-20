from fastapi import Depends, FastAPI
from sqlalchemy import select
from sqlalchemy.orm import Session

from .database import get_db
from . import models, schemas

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/categories", response_model=list[schemas.CategoryOut])
def list_categories(db: Session = Depends(get_db)):
    print("Fetching categories from the database...")
    return db.scalars(select(models.Category)).all()