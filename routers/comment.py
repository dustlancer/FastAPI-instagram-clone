from fastapi import APIRouter, status, HTTPException, Depends
from routers.schemas import CommentBase
from sqlalchemy.orm.session import Session
from db.database import get_db
from db.models import DbComment
from db import db_comment
from routers.schemas import UserAuth
from auth.oauth2 import get_current_user


router = APIRouter(
    prefix='/comment',
    tags = ['comment']
)


@router.get('/all/{post_id}')
def get_comments(post_id: int, db: Session = Depends(get_db)):
    return db_comment.get_all(db=db, post_id=post_id)


@router.post('')
def create(request: CommentBase, db: Session = Depends(get_db), current_user: UserAuth = Depends(get_current_user)):
    return db_comment.create(db=db, request=request)