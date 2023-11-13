from fastapi import FastAPI, Depends, HTTPException, status
import psycopg2
import time
from . import models, schemas
from .database import engine, get_db
from sqlalchemy.orm import Session

while True:

    try:
        conn = psycopg2.connect(host='20.168.252.45', 
                                database='Hubbard_Test', 
                                user='postgres', 
                                password='wigwag')
        cursor = conn.cursor()
        print("Database connection was successful")
        break

    except Exception as error:
        print("Connection to database failed")
        print("Error: ", error)
        time.sleep(2)

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/sqlalchemy")
def get_cities(db: Session = Depends(get_db)):
    cities = db.query(models.City).all()
    return {"cities": cities}


@app.post("/users", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def create_users(user: schemas.UserCreate, db: Session = Depends(get_db)):  
    new_user = models.User(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user