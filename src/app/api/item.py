import uuid
from fastapi import APIRouter
from pydantic import UUID4, BaseModel


router = APIRouter()


class ItemResponse(BaseModel):
    id : UUID4

@router.get("/items", response_model=ItemResponse, status_code=200, summary="Get items")
async def get_items() -> ItemResponse:
    return ItemResponse(id=uuid.uuid4())