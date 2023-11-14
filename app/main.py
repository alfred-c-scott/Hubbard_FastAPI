from fastapi import FastAPI, Depends, HTTPException, status
import psycopg2
import time
from . import models, schemas, utils
from .database import engine, get_db
from sqlalchemy.orm import Session
from .routers import user

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

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

app.include_router(user.router)

# @app.get("/")
# def root():
#     return {"message": "Hello World"}

# @app.get("/sqlalchemy")
# def get_cities(db: Session = Depends(get_db)):
#     cities = db.query(models.City).all()
#     return {"cities": cities}


# @app.post("/users", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
# def create_users(user: schemas.UserCreate, db: Session = Depends(get_db)):  
    
#     # hash the password
#     hashed_pwd = utils.hash(user.password)
#     user.password = hashed_pwd
    
#     new_user = models.User(**user.model_dump())
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)

#     return new_user


# @app.get('/users/{id}', response_model=schemas.UserOut)
# def get_user(id: int, db: Session = Depends(get_db)):
#     user = db.query(models.User).filter(models.User.id == id).first()

#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"user with id = {id} does not exist")
    
#     return user