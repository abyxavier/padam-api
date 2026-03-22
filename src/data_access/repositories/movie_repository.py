from src.data_access.interface.imovie_repository import IMovieRepository
from src.data_access.db.models import MovieTable
from src.business.entities.movie import Movie
from typing import List,Optional
from sqlalchemy.orm import Session
from sqlalchemy import func

class MovieRepository(IMovieRepository):
    def __init__(self,db:Session):
        self.db = db
        
    def get_movie_by_title(self, title:str)->Optional[Movie]:
        movie = self.db.query(MovieTable).filter(func.lower(MovieTable.title) == title.lower()).first()
        if not movie:
            return None
        return self._to_entity(movie)
    
    def get_all_movies(self)->List[Movie]:
        movies = self.db.query(MovieTable).all()
        return [self._to_entity(m) for m in movies]

    def add_movies(self,movies:List[Movie])->List[Movie]:
        db_movies=[MovieTable(
            title=movie.title,
            descrption=movie.description,
            genre=movie.genre,
            language=movie.language,
            embedding=movie.embedding
        ) for movie in movies]
        self.db.add_all(db_movies)
        self.db.commit()
        for m in db_movies:
            self.db.refresh(m)

        return [self._to_entity(m) for m in db_movies]

    def _to_entity(self, db_movie: MovieTable) -> Movie:
        return Movie(
            id=db_movie.id,
            title=db_movie.title,
            description=db_movie.descrption,
            genre=db_movie.genre,
            language=db_movie.language,
            embedding=db_movie.embedding
        )