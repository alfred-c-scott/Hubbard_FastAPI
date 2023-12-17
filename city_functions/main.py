from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
import json

Base = automap_base()

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@localhost/Hubbard_Test"

# engine, suppose it has two tables 'user' and 'address' set up
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# reflect the tables
Base.prepare(autoload_with=engine)

# mapped classes are now created with names by default
# matching that of the table name.
City = Base.classes.cities

session = Session(engine)
# cities = [
#     {
#         "country_code": "US",
#         "postal_code": "99553",
#         "city": "Akutan",
#         "state": "Alaska",
#         "state_code": "AK",
#         "admin_name_2": "Aleutians East",
#         "admin_code_2": "013",
#         "admin_name_3": "",
#         "admin_code_3": "",
#         "latitude": "54.143",
#         "longitude": "-165.7854",
#         "accuracy": "1"
#     },
#     {
#         "country_code": "US",
#         "postal_code": "99571",
#         "city": "Cold Bay",
#         "state": "Alaska",
#         "state_code": "AK",
#         "admin_name_2": "Aleutians East",
#         "admin_code_2": "013",
#         "admin_name_3": "",
#         "admin_code_3": "",
#         "latitude": "55.1858",
#         "longitude": "-162.7211",
#         "accuracy": "1"
#     },
#     {
#         "country_code": "US",
#         "postal_code": "99583",
#         "city": "False Pass",
#         "state": "Alaska",
#         "state_code": "AK",
#         "admin_name_2": "Aleutians East",
#         "admin_code_2": "013",
#         "admin_name_3": "",
#         "admin_code_3": "",
#         "latitude": "54.8542",
#         "longitude": "-163.4113",
#         "accuracy": "1"
#     },
#     {
#         "country_code": "US",
#         "postal_code": "99612",
#         "city": "King Cove",
#         "state": "Alaska",
#         "state_code": "AK",
#         "admin_name_2": "Aleutians East",
#         "admin_code_2": "013",
#         "admin_name_3": "",
#         "admin_code_3": "",
#         "latitude": "55.0628",
#         "longitude": "-162.3056",
#         "accuracy": "1"
#     },
#     {
#         "country_code": "US",
#         "postal_code": "99661",
#         "city": "Sand Point",
#         "state": "Alaska",
#         "state_code": "AK",
#         "admin_name_2": "Aleutians East",
#         "admin_code_2": "013",
#         "admin_name_3": "",
#         "admin_code_3": "",
#         "latitude": "55.3192",
#         "longitude": "-160.4914",
#         "accuracy": "1"
#     },
#     {
#         "country_code": "US",
#         "postal_code": "99546",
#         "city": "Adak",
#         "state": "Alaska",
#         "state_code": "AK",
#         "admin_name_2": "Aleutians West (CA)",
#         "admin_code_2": "016",
#         "admin_name_3": "",
#         "admin_code_3": "",
#         "latitude": "51.874",
#         "longitude": "-176.634",
#         "accuracy": "1"
#     }
# ]

with open ('US.json', 'r') as json_file:
    cities = json.load(json_file)

for city in cities:
    session.add(City(country_code=city['country_code'], 
                    zip_code=city['postal_code'], 
                    city_name=city['place_name'], 
                    state_name=city['admin_name_1'],
                    state_code=city['admin_code_1'],
                    admin_name_2=city['admin_name_2'],
                    admin_code_2=city['admin_code_2'],
                    admin_name_3=city['admin_name_3'],
                    admin_code_3=city['admin_code_3'],
                    latitude=city['latitude'],
                    longitude=city['longitude']))
    session.commit()
