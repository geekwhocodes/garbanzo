import uuid
from fastapi import APIRouter
from pydantic import UUID4, BaseModel


router = APIRouter()


class ItemResponse(BaseModel):
    id : UUID4


class ItemRequest(BaseModel):
    name : str
    email: str

@router.get("/items", response_model=ItemResponse, status_code=200, summary="Get items")
async def get_items() -> ItemResponse:
    return ItemResponse(id=uuid.uuid4())


@router.get("/item/{id}", response_model=dict, status_code=200, summary="Get items")
async def get_items(id:UUID4) -> ItemResponse:
    print(f"Getting item details for {id} from database.")
    return {
        "id" : id,
        "name" : "Makhaewf",
        "email" : "asdlkhj@,mndvbc.loin"
    }


@router.post("/items", response_model=ItemResponse, status_code=200, summary="Create item")
async def cteate_item(payload:ItemRequest) -> ItemResponse:
    print(payload)
    print(f"Stored in database!")
    return ItemResponse(id=uuid.uuid4())