from abc import ABC,abstractmethod
from src.models.movie import Movie
from src.models.recommendation import RecommendationResult
from typing import List

class IMovieRecommendationService(ABC):
    @abstractmethod
    def recommend(self,movie:str)->RecommendationResult:
        pass