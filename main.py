from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.presentation.api.controllers.health_controller import health_router, root_router
from src.presentation.api.controllers.recommend_controller import recommend_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health_router)
app.include_router(root_router)
app.include_router(recommend_router)

if __name__ == "__main__":
    import uvicorn
    # Pass "main:app" as a string instead of the app object so hot-reloading works properly when launching.
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)