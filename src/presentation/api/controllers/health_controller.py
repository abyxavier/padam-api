from fastapi import APIRouter,HTTPException,Request,status
from typing import Dict

health_router = APIRouter(
)

# Unprefixed router specifically to catch global cloud health checks (like Render)
@health_router.get("/")
@health_router.get("/health")
async def render_health_check() -> Dict[str, str]:
    return {"status": "Padam backend is healthy and running! 🚀"}

@health_router.get(
    "/ping",
    status_code=status.HTTP_200_OK,
    summary="Health Checkup ",
    description="Simple Ping Health checkup"
    )
async def ping() -> Dict[str,str]:
    """
    Simple Ping endpoint
    Returns:
        Dict[str,str]: _description_
    """
    return {"message":"pong"}