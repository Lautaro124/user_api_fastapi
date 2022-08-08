from fastapi import APIRouter
from fastapi_sqlalchemy import db

from models.models import Status
from schemas.shcemas import SchemaStatusUser

router = APIRouter(
    prefix='/status',
    tags=['👀 Status user']
)

@router.post('/status/create/status_user', response_model=SchemaStatusUser)
def post_status_user(status_user: SchemaStatusUser):
        db_status_user = Status(
            name= status_user.name,
            is_dangerous = status_user.is_dangerous
        )
        db.session.add(db_status_user)
        db.session.commit()
        return db_status_user