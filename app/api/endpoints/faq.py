"""
Методы api работы с Объектом FAQ
"""

from fastapi import APIRouter, Body, Header, Request
from fastapi.encoders import jsonable_encoder

from app.api.responses import create_response, bad_request, not_found, get_token_in_header
from app.api.schemas import Response_Base, Response_Q, Response_QAs, Response_QA_create, Response_QA_one, \
    QA_create, QA_update
from app.models import FAQ, PyObjectId, User

faq = APIRouter()


@faq.get('/all/', description='Получение всех вопросов + ответов', response_model=Response_QAs)
async def get_all_qa():
    """Все вопросы и ответы к ним."""

    data = await FAQ.all_data()
    return await create_response(data=data)


@faq.get('/questions/', description='Получение всех вопросов', response_model=Response_Q)
async def get_all_questions():
    """Все вопросы."""

    data = await FAQ.all_questions()
    return await create_response(data=data)


@faq.get('/answer/{_id: str}/', description='Получение ответа по вопросу', response_model=Response_QA_one)
async def get_answer(_id: str):
    """Ответ к вопросу по id объекта."""

    data = await FAQ.get_qa_from_id(_id)
    if data is None:
        return await not_found()
    return await create_response(data=data)


@faq.post('/create/', description='Создание новой записи вопрос + ответ', response_model=Response_QA_create)
async def create(request: Request, payload: QA_create = Body(...)):
    """Создание нового объекта (вопрос+ответ)."""

    user = await User.get_user(await get_token_in_header(request))
    if await User.is_manager(user):
        _id = await FAQ.create_qa(jsonable_encoder(payload), user)
        if _id is not None:
            return await create_response(data={'_id': _id}, message='New QA is created!')
        msg = 'Failed to save'
    else:
        msg = 'Not access'
    return await bad_request(msg)


@faq.put('/update/{_id: str}/', description='Редактирование существующей записи', response_model=Response_Base)
async def update(request: Request, _id, payload: QA_update = Body(...)):
    """Обновление существующего объекта по его id (обновление вопрос и/или ответ)."""

    user = await User.get_user(await get_token_in_header(request))
    if await User.is_manager(user):
        flg = await FAQ.update_qa(_id, jsonable_encoder(payload))
        if flg is None:
            return await not_found(f'_id=[{_id}]')
        elif flg:
            return await create_response(message=f'Updated _id=[{_id}] is success')
        msg = f'Updated _id=[{_id}] is failed'
    else:
        msg = 'Not access'
    return await bad_request(msg)


@faq.delete('/delete/{_id: str}/', description='Удаление записи', response_model=Response_Base)
async def delete(request: Request, _id: PyObjectId):
    """Удаление существующего объекта по его id."""

    user = await User.get_user(await get_token_in_header(request))
    if await User.is_manager(user):
        flg = await FAQ.delete_qa(_id)
        if flg is None:
            return await not_found(f'_id=[{_id}]')
        elif flg:
            return await create_response(message=f'Deleted _id=[{_id}] is success')
        msg = f'Deleted _id=[{_id}] is failed'
    else:
        msg = 'Not access'
    return await bad_request(msg)
