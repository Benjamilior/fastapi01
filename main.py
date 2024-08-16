from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from typing import Optional
from bd.database import SessionLocal, engine, Base
from models.models import Movie as MovieModel
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter
from routers.movie import routmovie
class Movie(BaseModel):
    id: Optional[int] = None
    tittle: str
    overview: str
    year: int
    rating: float
    category: str

Base.metadata.create_all(bind=engine)




app = FastAPI(
    title="Primer Test",
    description="Primer Test",
    version="0.0.1",
)

app.include_router(routmovie)

# @app.get("/movies", tags=["movie"])
# def get_movies():
#     return movies

# @app.get("/movies/{id}" , tags=["movie"])
# def get_movies(id:int):
#     for item in movies:
#         if item["id"] == id:
#             return item

# @app.get("/movies/", tags=["movie"])
# def get_movies_by_category(category: str):
#     # Filtrar las películas por categoría (case insensitive)
#     filtered_movies = [movie for movie in movies if movie["category"].lower() == category.lower()]
    
#     if not filtered_movies:
#         raise HTTPException(status_code=404, detail="No movies found in this category")
    
#     return filtered_movies

