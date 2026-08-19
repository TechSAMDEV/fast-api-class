from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI()

# 1. Define Pydantic models for request bodies
class ItemCreate(BaseModel):
    id: int
    item: str
    status: str
    price: float

class ItemUpdate(BaseModel):
    item: str
    status: str
    price: float

# Global in-memory data store
all_items = []

@app.get("/")
async def inventory():
    return all_items

# 2. Fixed: Accept Pydantic model payload for JSON data
@app.post("/create_items", status_code=status.HTTP_201_CREATED)
async def create_items(id, item, status, price):
    new_item = {"id": id, "item": item, "status": status, "price": price}
    all_items.append(new_item)
    return {"items": all_items}

# 3. Fixed: Uses ItemUpdate body so fields don't accidentally become query parameters
@app.put("/update_item/{item_id}")
async def update_item(item_id: int, updated_data: ItemUpdate):
    for existing_item in all_items:
        if existing_item["id"] == item_id:
            existing_item["item"] = updated_data.item
            existing_item["status"] = updated_data.status
            existing_item["price"] = updated_data.price
            return {"message": "Item updated", "item": existing_item}
            
    raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/delete_item/{item_id}")
async def delete_item(item_id: int):
    for index, existing_item in enumerate(all_items):
        if existing_item["id"] == item_id:
            deleted_item = all_items.pop(index)
            return {"message": "Item deleted", "item": deleted_item}
            
    raise HTTPException(status_code=404, detail="Item not found")
