from fastapi import FastAPI
from app.routes.auth_routes import auth_router
from app.routes.hotel_routes import hotel_router
from app.routes.item_routes import item_router
from app.routes.hotel_item_routes import hotel_items_router
from app.routes.item_delete_router import hotel_items_delete_router

app = FastAPI()
app.include_router(auth_router, prefix="/auth")
app.include_router(hotel_router, prefix="/hotel")
app.include_router(item_router, prefix="/item")
app.include_router(hotel_items_router, prefix="/hotel-items")
app.include_router(hotel_items_delete_router, prefix="/hotel-items")