from fastapi import APIRouter, HTTPException, Path
from app.database import get_db_connection

hotel_items_delete_router = APIRouter()

@hotel_items_delete_router.delete("/delete-dish/{item_id}")
def delete_dish(item_id: int = Path(..., description="The ID of the dish to delete")):
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        cur.execute("DELETE FROM hotel_items WHERE item_id = %s", (item_id,))
        
        if cur.rowcount == 0:
            raise HTTPException(status_code=404, detail="Dish not found.")
        
        conn.commit()
        return {"message": f"Dish with ID {item_id} deleted successfully."}
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=f"Failed to delete dish: {str(e)}")
    finally:
        cur.close()
        conn.close()
# This code defines a FastAPI router for deleting a dish from the hotel items database.
# It includes a DELETE endpoint that takes an item ID as a path parameter and deletes the corresponding dish from the database.