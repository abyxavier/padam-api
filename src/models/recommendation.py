from pydantic import BaseModel,Field
from typing import List

class RecommendedMovie(BaseModel):
    movie : str =Field(...,example="Dune")
    reason : str =Field(...,example="Because you liked 'Dune'")
    
class RecommendationRequest(BaseModel):
    movie :str =Field(...,example="Dune")

class RecommendationResult(BaseModel):
    movie_list: List[RecommendedMovie]
    