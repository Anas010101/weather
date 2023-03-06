from models import Weather, WeatherStats, get_db
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

app = FastAPI(title="Weather App", debug=True)

@app.get("/api/weather")
async def get_weather(db: Session = Depends(get_db), limit: int = 10, page: int = 1, year: int = 0, city: str = ""):
    skip = (page - 1) * limit
    q = db.query(Weather)
    if year != 0:
        q = q.filter(Weather.date >= str(year)+'-01-01').filter(Weather.date <= str(year)+'-12-31')
    if city != 0:
        q = q.filter(Weather.city_code == city)
    temperatures = q.limit(limit).offset(skip).all()
    return {'status': 'success', 'results': db.query(Weather).count(), 'weathers': temperatures }


@app.get("/api/weather/stats")
async def get_weather_stats(db: Session = Depends(get_db), limit: int = 10, page: int = 1, year: int = 0, city: str = ""):
    skip = (page - 1) * limit
    q = db.query(WeatherStats)
    if year != 0:
        q = q.filter(WeatherStats.year == year)
    if city != 0:
        q = q.filter(WeatherStats.city_code == city)
    stats = q.limit(limit).offset(skip).all()
    return {'status': 'success', 'results': db.query(WeatherStats).count(), 'stats': stats }