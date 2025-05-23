from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.database import get_db_connection

hotel_items_router = APIRouter()

class DishStatusUpdate(BaseModel):
    item_id: int
    status: bool

@hotel_items_router.put("/update-dish-status")
def update_dish_status(data: DishStatusUpdate):
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        cur.execute("""
            UPDATE hotel_items
            SET status = %s
            WHERE item_id = %s
        """, (data.status, data.item_id))
        
        if cur.rowcount == 0:
            raise HTTPException(status_code=404, detail="Dish not found.")
        
        conn.commit()
        return {"message": f"Dish status updated to {'Available' if data.status else 'Unavailable'}."}
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=f"Failed to update dish status: {str(e)}")
    finally:
        cur.close()
        conn.close()
