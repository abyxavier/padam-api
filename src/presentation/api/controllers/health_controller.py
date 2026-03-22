from fastapi import APIRouter,HTTPException,Request,status
from typing import Dict

health_router=APIRouter(
    prefix="/api/v1/health",tags=["Health"]
)

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