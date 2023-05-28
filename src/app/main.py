from fastapi import Depends, FastAPI
import uvicorn

from app.config import Settings, get_settings

app : FastAPI = FastAPI()

@app.get("/item")
def read_item(settings: Settings = Depends(get_settings)) -> int:
    return 1

@app.get("/health")
def health() -> bool:
    return True

# if __name__ == "__main__":
#     uvicorn.run(app=app, host="0.0.0.0", port=8000, reload=False)
