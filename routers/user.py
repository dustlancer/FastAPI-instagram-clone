from urllib import request
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm.session import Session
from db.database import get_db
from .schemas import UserBase, UserDisplay, UserAvatarSet
from db import db_user
from routers.schemas import UserAuth
from auth.oauth2 import get_current_user

router = APIRouter(
    prefix='/user',
    tags=['user']
)

image_url_types = ['absolute', 'relative']


@router.get('/')
def get_users(db: Session = Depends(get_db)):
    return db_user.get_users(db)

@router.post('/', response_model=UserDisplay)
def create_user(request: UserBase, db:Session = Depends(get_db)):
    return db_user.create_user(request=request, db=db)


@router.post('/set_avatar')
def set_avatar(request: UserAvatarSet, db:Session = Depends(get_db), current_user: UserAuth = Depends(get_current_user)):
    if not request.avatar_url_type in image_url_types:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                            detail="Parameter image_url_type can only take values 'absolute' or 'relative'")
    return db_user.set_avatar(db=db, user_id=current_user.id, request=request)