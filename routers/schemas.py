from pydantic import BaseModel
from datetime import datetime
from typing import List

class UserBase(BaseModel):
    username: str
    email: str
    password: str

class UserDisplay(BaseModel):
    username: str
    email: str

class PostBase(BaseModel):
    image_url: str
    image_url_type: str
    caption: str
    creator_id: int

class PostCreate(BaseModel):
    image_url: str
    image_url_type: str
    caption: str

# for PostDisplay
class User(BaseModel):
    username: str

# for PostDisplay
class Comment(BaseModel):
    text: str
    username: str    
    timestamp: datetime

class PostDisplay(BaseModel):
    id: int
    image_url: str
    image_url_type: str
    caption: str
    timestamp: datetime
    user: User
    comments: List[Comment]


class UserAuth(BaseModel):
    id: int
    username: str
    email: str


class CommentBase(BaseModel):
    username: str
    text: str
    post_id: str

