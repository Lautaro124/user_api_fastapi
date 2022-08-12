from fastapi import APIRouter
from fastapi_sqlalchemy import db

from models.models import User
from schemas.shcemas import SchemaUser

router = APIRouter(
    prefix='/user',
    tags=['👤 User']
)

@router.get('/user/get_all_users')
def get_all_users():
    users = db.session.query(User).all()
    return users

@router.post('/create', response_model=SchemaUser)
async def post_user(user: SchemaUser):
        db_user = User(
            name= user.name, 
            age= user.age, 
            status_id= user.status_id
        )
        db.session.add(db_user)
        db.session.commit()
        return db_user