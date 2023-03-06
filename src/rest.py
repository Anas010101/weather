from models import Weather, WeatherStats, get_db
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

app = FastAPI(title="Weather App", debug=True)

@app.get("/api/weather")
async def get_weather(db: Session = Depends(get_db), limit: int = 10, page: int = 1):
    skip = (page - 1) * limit
    temperatures = db.query(Weather).limit(limit).offset(skip).all()
    return {'status': 'success', 'results': db.query(Weather).count(), 'weathers': temperatures }


@app.get("/api/weather/stats")
async def get_weather_stats(db: Session = Depends(get_db), limit: int = 10, page: int = 1):
    skip = (page - 1) * limit
    stats = db.query(WeatherStats).limit(limit).offset(skip).all()
    return {'status': 'success', 'results': db.query(WeatherStats).count(), 'stats': stats }