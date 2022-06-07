"""
Методы api
"""

from fastapi import APIRouter

from app.api.responses import create_response
from app.api.schemas import Response_Base

home = APIRouter()


@home.get('/', response_model=Response_Base)
async def main():
    """Home route."""
    return await create_response(message='hello this is home route')
