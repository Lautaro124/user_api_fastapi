import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_sqlalchemy import DBSessionMiddleware, db
from dotenv import load_dotenv

from routes import router_index


load_dotenv(".env")

tag_metadata= [
    {"name": "👤 User", "description": "endpoint user data"},
    {"name": "👀 Status user", "description": "endpoint of status user"},
]

app = FastAPI(
    openapi_tags=tag_metadata,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])

app.include_router(router_index.router)

@app.get("/")
async def initialize():
    return {"message": "Iniciado"}


