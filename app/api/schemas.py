"""
Schemas for response API.
"""

from datetime import datetime, time
from typing import List, Optional, Dict


from app.models.user import User
from config.config import Config

from pydantic import BaseModel, validator


class Q_Base(BaseModel):
    id: str
    update_dt: Optional[datetime or None]


class Q(Q_Base):
    question: str


class QAs(Q, Q_Base):
    answer: str


class QA_one(QAs):
    create_dt: Optional[datetime or None]


class QA_create(BaseModel):
    question: str
    answer: str


class QA_update(BaseModel):
    question: Optional[str] = None
    answer: Optional[str] = None


class Response_Base(BaseModel):
    code: int = 200
    message: str = ''
    data: Optional[Dict or List] = None


class Response_Q(Response_Base):
    data: List[Optional[Q]]


class Response_QAs(Response_Base):
    data: List[Optional[QAs]]


class Response_QA_one(Response_Base):
    data: Optional[QA_one]


class Response_QA_create(Response_Base):
    data: Optional[Dict]



class User_token_update(BaseModel):
    uid: str
    token: str
    expiration_dt: datetime

class User_update_all(BaseModel):
    __root__: List[User]  # ⯇-- __root__
