from typing import Optional
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id:int, q:Optional[str] = None):
    return {"item_id":item_id, "q":q}

@app.post("/multiply")
async def multiply(a: int, b: int):
    return {"result": a * b}