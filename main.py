# main.py

from fastapi import FastAPI
from api.routes import ask_router

app = FastAPI(title="Osmigo Core")

app.include_router(ask_router, prefix="/ask")
