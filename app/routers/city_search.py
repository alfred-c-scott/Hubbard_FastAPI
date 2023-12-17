# 3rd party imports
from fastapi import Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
# local imports
from .. import models, schemas, utils, database, oauth2


router = APIRouter(
    # prefix="/city",
    # tags=["Posts"]
)

@router.get("/city/{zip}", response_model=schemas.City)
def get_city(zip: str, 
             db: Session = Depends(database.get_db),
             user_id: int = Depends(oauth2.get_current_user)):
    # zip = 63660
    print(zip)
    city = db.query(models.City).filter(models.City.zip_code == zip).first()

    return city