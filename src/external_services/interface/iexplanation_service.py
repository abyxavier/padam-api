from abc import ABC,abstractmethod
from src.models.movie import Movie


class IExplanationService(ABC):
    @abstractmethod
    def explain_reason(
        self,
        input_movie:Movie,
        recommended_movie:Movie,
        similarity_score:float
    )->str:
        pass