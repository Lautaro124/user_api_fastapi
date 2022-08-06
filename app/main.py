import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def initialize():
    return {'message': 'Iniciado'}