from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from typing import Optional
from bd.database import SessionLocal, engine, Base
from models.models import Movie as MovieModel
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter

class Movie(BaseModel):
    id: Optional[int] = None
    tittle: str
    overview: str
    year: int
    rating: float
    category: str
    
routmovie = APIRouter()

@routmovie.get("/movieslol/", tags=["movie"])
def get_movies():
    bd= SessionLocal()
    data = bd.query(MovieModel).all()
    return JSONResponse(content=jsonable_encoder(data))

@routmovie.get("/moviesbyid/{id}", tags=["movie"])
def get_movie(id: int):
    bd= SessionLocal()
    data = bd.query(MovieModel).filter(MovieModel.id == id).first()
    if not data:
        raise HTTPException(status_code=404, detail="Movie not found")
    return JSONResponse(content=jsonable_encoder(data))

@routmovie.post("/movies", tags=["movie"])
def create_movie(movie: Movie): 
    bd=SessionLocal()
    newMovie = MovieModel(**movie.dict())
    bd.add( newMovie )
    bd.commit()
    return JSONResponse(status_code=201, content=movie.dict())

@routmovie.get("/movies/{id}", tags=["movie"])
def get_movie_by_category(category:str):
    bd=SessionLocal()
    data = bd.query(MovieModel).filter(MovieModel.category == category).all()
    return JSONResponse(content=jsonable_encoder(data))

@routmovie.put("/movies/{id}", tags=["movie"],status_code=200)
def update_movie(id: int, movie: Movie):
    bd=SessionLocal()
    data = bd.query(MovieModel).filter(MovieModel.id == id).first()
    if not data:
        raise HTTPException(status_code=404, detail="Movie not found")
    data.title = movie.tittle
    data.overview = movie.overview
    data.year = movie.year
    data.rating = movie.rating
    data.category = movie.category
    bd.commit()
    return JSONResponse(status_code=200, content=movie.dict())

@routmovie.delete("/movies/{id}", tags=["movie"], status_code=200)
def delete_movie(id: int):
    bd=SessionLocal()
    data = bd.query(MovieModel).filter(MovieModel.id == id).first()
    if not data:
        raise HTTPException(status_code=404, detail="Movie not found")
    bd.delete(data)
    bd.commit()
    return JSONResponse(status_code=200, content={'message': 'Movie deleted','data': jsonable_encoder(data)}) 
                        
                        
                     