

movie_router = APIRouter(
    prefix="/api/v1/movies", tags=["Movies"]
)

@movie_router.get("/stats",status_code=status.HTTP_200_OK, 
                        response_model=List[Movie], 
                        summary="Get all movie stats including language total count and genre that are aviable now",
                        description="Get all movie stats including language total count and genre that are aviable now")
def get_all_movies():
    with get_db() as db:
        movie_service = MovieService(db)
        return movie_service.get_all_movies()