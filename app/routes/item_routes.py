from fastapi import APIRouter, HTTPException
from app.database import get_db_connection
from app.models.item_models import HotelItemCreate

item_router = APIRouter()

@item_router.post("/add")
def add_item(item: HotelItemCreate):
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        cur.execute("""
            INSERT INTO hotel_items (
                u_id, dish_name, dish_type, dish_description,
                img_1, img_2, rate, food_type
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            item.u_id, item.dish_name, item.dish_type,
            item.dish_description, item.img_1, item.img_2,
            item.rate, item.food_type
        ))
        conn.commit()
        return {"message": "Item added successfully"}
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=f"Error adding item: {str(e)}")
    finally:
        cur.close()
        conn.close()
