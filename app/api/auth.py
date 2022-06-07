"""
Авторизация к API
"""

from fastapi import Depends
from fastapi.security import HTTPBasicCredentials, HTTPBearer

from app.api.responses import unauthorized
from app.models import User

security = HTTPBearer()


async def has_access(credentials: HTTPBasicCredentials = Depends(security)):
    """Function that is used to validate the token in the case that it requires it"""
    from app import conf
    if credentials.credentials != conf.API_TOKEN:
        msg = 'Не верное значение токена'
        return await unauthorized(msg)


authorization = [Depends(has_access)]
