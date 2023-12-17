from fastapi import FastAPI, Depends, HTTPException, status
import psycopg2
import time
from . import models, schemas, utils
from .database import engine, get_db
from sqlalchemy.orm import Session
from .routers import user, auth, city_search

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

while True:

    try:
        conn = psycopg2.connect(host='127.0.0.1', 
                                database='Hubbard_Test', 
                                user='postgres', 
                                password='postgres')
        cursor = conn.cursor()
        print("Database connection was successful")
        break

    except Exception as error:
        print("Connection to database failed")
        print("Error: ", error)
        time.sleep(2)

app.include_router(city_search.router)
app.include_router(user.router)
app.include_router(auth.router)