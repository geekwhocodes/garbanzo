from fastapi import Depends, FastAPI
import uvicorn
from app.api import init, item

from app.config import Settings, get_settings

def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(init.router)
    app.include_router(item.router)
    return app

app : FastAPI = create_app()

# if __name__ == "__main__":
#     uvicorn.run(app=app, host="0.0.0.0", port=8000, reload=False)
