from src.models.movie import Movie
from src.external_services.interface.iexplanation_service import IExplanationService

class ExplanationService(IExplanationService):
    def explain_reason(
        self,
        input_movie: Movie,
        recommended_movie: Movie,
        similarity_score: float
    ) -> str:

        return (
            f"Because you liked '{input_movie.title}', "
            f"'{recommended_movie.title}' shares similar themes and tone. "
            f"Similarity score: {round(similarity_score, 3)}."
        )