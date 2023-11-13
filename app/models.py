from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import REAL
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP

from .database import Base

class City(Base):
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, nullable=False)
    country_code = Column(String, nullable=False, default="country_code_default")
    zip_code = Column(String, nullable=False, default='00000')
    city_name = Column(String, nullable=False, default='city_name_default')
    state_name = Column(String, nullable=False, default='state_name_default')
    state_code = Column(String, nullable=False, default='state_code_default')
    admin_name_2 = Column(String, nullable=False, default='admin_name_2_default')
    admin_code_2 = Column(String, nullable=False, default='admin_code_2_default')
    admin_name_3 = Column(String, nullable=False, default='admin_name_3_default')
    admin_code_3 = Column(String, nullable=False, default='admin_code_3_default')
    latitude = Column(REAL, nullable=False, server_default='0.0000')
    longitude = Column(REAL, nullable=False, server_default='0.0000')
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))

class User(Base):
    __tablename__ = "users"

    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    id = Column(Integer, primary_key=True, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))