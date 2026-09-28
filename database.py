# sessionmaker()
# create_engine()
# declarative_base()
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine=create_engine("sqlite:///./restaurant.db")
#for sqlite:- sqlite:///./dbname
#for mysql:- mysql+mysqlconnector://username:password@localhost:port/database_name
# mysql+mysqlconnector://test:Test%40123@localhost:3309/fastapi
# by default port is 3306
# if password has @ :- instead of @ we use %40

LocalSession=sessionmaker(bind=engine,
                          autoflush=True)

Base = declarative_base()