import os

from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware, db
from dotenv import load_dotenv

from models import Status, User
from shcemas import SchemaStatusUser, SchemaUser

load_dotenv('.env')

app = FastAPI()
app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])

@app.get('/')
async def initialize():
    return {'message': 'Iniciado'}

@app.get('/get_all_users')
def get_all_users():
    users = db.session.query(User).all()
    return users

@app.post('/create/user', response_model=SchemaUser)
async def post_user(user: SchemaUser):
        db_user = User(
            name= user.name, 
            age= user.age, 
            status_id= user.status_id
        )
        db.session.add(db_user)
        db.session.commit()
        return db_user


@app.post('/create/status_user', response_model=SchemaStatusUser)
def post_status_user(status_user: SchemaStatusUser):
        db_status_user = Status(
            name= status_user.name,
            is_dangerous = status_user.is_dangerous
        )
        db.session.add(db_status_user)
        db.session.commit()
        return db_status_user
