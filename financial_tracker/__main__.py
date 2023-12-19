from fastapi import FastAPI
import uvicorn
import financial_tracker
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/items/{item_id}")
async def read_item(item_id: str):
    items = {"banana": 2, "apple": 3, "orange": 4}
    if item_id not in items:
        return 1
    return items[item_id]


def main():
    uvicorn.run(
        "financial_tracker.__main__:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        reload_dirs=["financial_tracker"],
        reload_includes=["*.py"],
    )


if __name__ == "__main__":
    main()
