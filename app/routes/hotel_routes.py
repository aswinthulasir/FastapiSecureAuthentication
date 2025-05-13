from fastapi import APIRouter, HTTPException
from app.database import get_db_connection
from app.models.hotel_models import HotelRegister

hotel_router = APIRouter()

@hotel_router.post("/register")
def register_hotel(hotel: HotelRegister):
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        cur.execute("""
            INSERT INTO hotels (u_id, hotel_name, hotel_address, hotel_contact, hotel_type)
            VALUES (%s, %s, %s, %s, %s)
        """, (hotel.u_id, hotel.hotel_name, hotel.hotel_address, hotel.hotel_contact, hotel.hotel_type))
        conn.commit()
        return {"message": "Hotel registered successfully"}
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=f"Failed to register hotel: {str(e)}")
    finally:
        cur.close()
        conn.close()
