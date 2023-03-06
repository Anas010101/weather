from typing import Iterator
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, Float
from sqlalchemy.orm import Session, sessionmaker
from utils import init


conn = init("../.env")

SessionLocal = sessionmaker(autocommit=True, autoflush=True, bind=conn)
Base = declarative_base(bind=conn)

class Weather(Base):
    __tablename__ = "temperature_history"
    city_code = Column(String, primary_key=True)
    date = Column(Date, primary_key=True)
    maximum = Column(Integer)
    minimum = Column(Integer)
    precipitation = Column(Integer)

class WeatherStats(Base):
        __tablename__ = "temperature_statistics"
        city_code = Column(String, primary_key=True)
        year = Column(Integer, primary_key=True)
        maximum_average = Column(Float)
        minimum_average = Column(Float)
        accumulated_precipitation = Column(Float)

def get_db() -> Iterator[Session]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
