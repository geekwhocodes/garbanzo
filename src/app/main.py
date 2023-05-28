from fastapi import FastAPI
import uvicorn

app : FastAPI = FastAPI()

@app.get("/item")
def read_item() -> int:
    return 1

@app.get("/health")
def health() -> bool:
    return True

# if __name__ == "__main__":
#     uvicorn.run(app=app, host="0.0.0.0", port=8000, reload=False)
