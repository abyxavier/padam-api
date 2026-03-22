from abc import ABC,abstractmethod
from src.models.movie import Movie
from typing import List,Optional
class IMovieRepository(ABC):
    
    @abstractmethod
    def get_movie_by_title(self,title:str)-> Optional[Movie]:
        pass
    
    @abstractmethod
    def get_all_movies(self)->List[Movie] | None:
        pass
    