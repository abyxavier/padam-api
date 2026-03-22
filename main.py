from fastapi import FastAPI
from src.presentation.api.controllers.health_controller import health_router
from src.presentation.api.controllers.recommend_controller import recommend_router

app=FastAPI()   

app.include_router(health_router)
app.include_router(recommend_router)
