from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

Base = automap_base()
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@localhost/hubbard"
# engine, suppose it has two tables 'user' and 'address' set up
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# reflect the tables
Base.prepare(autoload_with=engine)

# mapped classes are now created with names by default
# matching that of the table name.
City = Base.classes.cities

session = Session(engine)

session.add(City(country_code="US", 
                 zip_code="44444", 
                 city_name="Lexington", 
                 state_name="Kentucky",
                 state_code="KY",
                 latitude="0.0000",
                 longitude="0.0000"))
session.commit()
