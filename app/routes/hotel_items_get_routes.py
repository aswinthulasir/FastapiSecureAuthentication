from fastapi import APIRouter, HTTPException, Query
from app.database import get_db_connection

hotel_items_get_router = APIRouter()

@hotel_items_get_router.get("/")
def get_all_dishes(u_id: str = Query(..., description="User ID of the hotel to fetch dishes for")):
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        cur.execute("""
            SELECT 
                item_id,
                u_id,
                dish_name,
                dish_type,
                dish_description,
                img_1,
                img_2,
                rate,
                food_type,
                status
            FROM hotel_items
            WHERE u_id = %s
            ORDER BY item_id
        """, (u_id,))
        
        rows = cur.fetchall()
        if not rows:
            raise HTTPException(status_code=404, detail="No dishes found for the provided user ID.")

        dishes = []
        for row in rows:
            dishes.append({
                "item_id": row[0],
                "u_id": row[1],
                "dish_name": row[2],
                "dish_type": row[3],
                "dish_description": row[4],
                "img_1": row[5],
                "img_2": row[6],
                "rate": float(row[7]),
                "food_type": row[8],
                "status": row[9],
            })

        return {"dishes": dishes}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch dishes: {str(e)}")
    finally:
        cur.close()
        conn.close()
