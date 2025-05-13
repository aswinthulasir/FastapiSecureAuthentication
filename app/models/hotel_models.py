from pydantic import BaseModel, Field

class HotelRegister(BaseModel):
    u_id: str = Field(..., min_length=16, max_length=16)
    hotel_name: str
    hotel_address: str
    hotel_contact: str
    hotel_type: int
