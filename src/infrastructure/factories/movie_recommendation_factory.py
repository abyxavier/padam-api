from src.business.services.movie_recommendation_service import MovieRecommendationService
from src.data_access.repositories.movie_repository import MovieRepository
from src.external_services.service.explanation_service import ExplanationService
from sqlalchemy.orm import Session

class MovieRecommendationFactory:

    @staticmethod
    def create(db:Session) -> MovieRecommendationService:
        repository = MovieRepository(db)
        explanation=ExplanationService()
        return MovieRecommendationService(movie_repository=repository,explanation_service=explanation)

