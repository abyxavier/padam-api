from fastapi import APIRouter, HTTPException,status
from src.models.recommendation import RecommendationResult, RecommendationRequest
from src.infrastructure.factories.movie_recommendation_factory import MovieRecommendationFactory
from src.data_access.db.session import get_db

recommend_router = APIRouter(
    prefix="/api/v1/recommend", tags=["Recommend"]
)

@recommend_router.post("/",status_code=status.HTTP_200_OK, 
                        response_model=RecommendationResult, 
                        summary="Recommend movies based on the input movie name. Type in the movie name directly with correct alphabet",
                        description="Recommend Realted Movies with given input movie eg: \n{\"movie\": \"Dune\"}")
def recommend(request: RecommendationRequest):
    try:
        with get_db() as db:
            recommend_service = MovieRecommendationFactory.create(db)
            return recommend_service.recommend(request.movie)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
        