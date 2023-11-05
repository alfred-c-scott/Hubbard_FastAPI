from fastapi import FastAPI, Depends
import psycopg2
from . import models
from .database import engine, get_db
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/sqlalchemy")
def get_cities(db: Session = Depends(get_db)):
    cities = db.query(models.City).all()
    return {"cities": cities}
