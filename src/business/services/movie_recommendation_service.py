from src.business.interface.imovie_recommendation_service import IMovieRecommendationService
from src.data_access.interface.imovie_repository import IMovieRepository
from src.external_services.interface.iexplanation_service import IExplanationService
from src.models.recommendation import RecommendationResult,RecommendedMovie
from src.utilities.embedding import parse_embedding
from src.utilities.similarity import cosine_similarity
from typing import List

class MovieRecommendationService(IMovieRecommendationService):
    def __init__(self,
                movie_repository:IMovieRepository,
                explanation_service:IExplanationService):
        self._movie_repository = movie_repository
        self.explanation_service=explanation_service
    
    def recommend(self, title: str) -> RecommendationResult:
        input_movie = self._movie_repository.get_movie_by_title(title)
        if not input_movie:
            raise ValueError("Movie not found")

        input_embedding = parse_embedding(input_movie.embedding)
        movies_list = self._movie_repository.get_all_movies()

        # Step 1: Score ALL movies first (fast — just math, no explanation yet)
        scored_movies = []
        for movie in movies_list:
            if movie.id == input_movie.id:
                continue
            movie_embedding = parse_embedding(movie.embedding)
            similarity_score = cosine_similarity(input_embedding, movie_embedding)
            scored_movies.append({"movie": movie, "similarity_score": similarity_score})

        # Step 2: Sort and pick top 5 only
        scored_movies.sort(key=lambda x: x["similarity_score"], reverse=True)
        top_n = scored_movies[:5]

        # Step 3: Only explain the top 5 (not every movie in DB)
        return RecommendationResult(
            movie_list=[
                RecommendedMovie(
                    movie=item["movie"].title,
                    reason=self.explanation_service.explain_reason(
                        input_movie, item["movie"], item["similarity_score"]
                    )
                )
                for item in top_n

            ]
        )