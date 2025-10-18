from fastapi import FastAPI
from schemas import Item

app = FastAPI()

@app.post("/items/")
async def create_item(item: Item):
    total = item.price + (item.tax or 0)
    return {"name":item.name, "total":total}