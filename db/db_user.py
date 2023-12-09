from sqlalchemy import null
from routers.schemas import User, UserBase, UserAvatarSet
from sqlalchemy.orm.session import Session
from .models import DbUser
from db.hashing import Hash
from fastapi import HTTPException, status


def get_users(db:Session):
    users = db.query(DbUser).all()
    return users

def create_user(db: Session, request: UserBase):
    new_user = DbUser(
        username = request.username,
        email = request.email,
        password = Hash.bcrypt(request.password), # we need to hash the psw
        avatar_url = None,
        avatar_url_type = None
    ) 

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
 

def get_user_by_username(db: Session, username: str):
    user = db.query(DbUser).filter(DbUser.username == username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User with username {username} not found')
    return user


def set_avatar(db: Session, user_id: int, request: UserAvatarSet):
    user = db.query(DbUser).filter(DbUser.id == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User with id {user_id} not found')
    user.avatar_url = request.avatar_url
    user.avatar_url_type = request.avatar_url_type
    db.commit()

    return user


def get_profile(db: Session, user_id: int, current_user_id: int = 0):
    user = db.query(DbUser).filter(DbUser.id == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User with id {user_id} not found')
    return user