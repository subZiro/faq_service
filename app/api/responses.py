"""
Response API
"""

from fastapi import HTTPException, Request
from typing import Any


async def create_response(data: Any = None, code: int = 200, message: str = "") -> dict:
    """
    Шаблон ответа для методов АПИ.

    :param data: Any: содержимое data
    :param code: int: код ответа
    :param message: str: сообщение
    :return: Response: dict:
    """
    return {"data": data, "code": code, "message": message}


async def bad_request(message='Bad request') -> HTTPException:
    """
    Response 400

    :param message: str:
    :return: json:
    """
    raise HTTPException(status_code=400, detail=message)


async def unauthorized(message='unauthorized') -> HTTPException:
    """
    Response 401

    :param message: str:
    :return: json:
    """
    raise HTTPException(status_code=401, detail=message)


async def forbidden(message='forbidden') -> HTTPException:
    """
    Response 403

    :param message: str:
    :return: json:
    """
    raise HTTPException(status_code=403, detail=message)


async def not_found(message='Object not found') -> HTTPException:
    """
    Response 404

    :param message: str:
    :return: json:
    """
    raise HTTPException(status_code=404, detail=message)


async def get_token_in_header(request: Request) -> str:
    """
    Извлечение токена из заголовка запроса.

    :param request: Request:
    :return token: str:
    """

    my_header = request.headers['authorization']
    return my_header.replace('Bearer ', '')
