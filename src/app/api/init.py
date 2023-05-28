from fastapi import APIRouter
from pydantic import BaseModel


router = APIRouter()

class HealthResponse(BaseModel):
    status : str


@router.get("/health", status_code=200, response_model=HealthResponse)
async def health() -> HealthResponse:
    return HealthResponse(status="healthy")