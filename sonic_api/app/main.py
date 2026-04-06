from fastapi import FastAPI
from app.routes import sonic_routes

app = FastAPI()

app.include_router(sonic_routes.router)