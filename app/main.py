from fastapi import FastAPI
from app.routes.auth_routes import auth_router
from app.routes.hotel_routes import hotel_router

app = FastAPI()
app.include_router(auth_router, prefix="/auth")
app.include_router(hotel_router, prefix="/hotel")