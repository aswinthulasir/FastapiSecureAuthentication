from pydantic import BaseModel

class HotelItemCreate(BaseModel):
    u_id: str
    dish_name: str
    dish_type: int
    dish_description: str
    img_1: str
    img_2: str
    rate: float
    food_type: int
