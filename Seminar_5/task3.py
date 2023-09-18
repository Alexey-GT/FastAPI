import uvicorn as uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

movies = []


class Movie(BaseModel):
    id: int
    title: str
    description: str
    genre: str


class MovieIn(BaseModel):
    title: str
    description: str
    genre: str


@app.post("/movie/", response_model=Movie)
async def create_movie(new_movie: MovieIn):
    movies.append(
        Movie(id=len(movies) + 1, title=new_movie.title, description=new_movie.description, genre=new_movie.genre)
    )
    return movies[-1]


@app.get("/movies/{genre}", response_model=list[Movie])
async def get_movies(genre: str):
    result = []
    for movie in movies:
        if movie.genre == genre:
            result.append(movie)
    return result


if __name__ == "__main__":
    uvicorn.run("task_2:app", host="127.0.0.1", port=8000, reload=True)