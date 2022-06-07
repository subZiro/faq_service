"""FAQ mock DB Object"""

from datetime import datetime
from typing import Optional, List, Dict

from app import logger
from app.common import now_dt
from app.database import db

from app.models.common import BaseDBModel, PyObjectId

logger = logger.getChild('models.faq')


class FAQ(BaseDBModel):
    """Модель хранения вопрос-ответ объекта."""
    id: PyObjectId
    question: Optional[str]
    answer: Optional[str]
    create_dt: Optional[datetime]
    update_dt: Optional[datetime]

    class Config:
        schema_extra = {
            "example": {
                'id': '6271097f35d7d379f1b642b4',
                'question': 'test question 1',
                'answer': 'test answer 1',
                'create_dt': '',
                'update_dt': '',
            }
        }

    @staticmethod
    def item(row) -> dict:
        """
        Метод для преобразования обхекта в удобный формат dict.

        :param row:
        :return: dict:
        """
        return {'id': row['_id'].__str__(),
                'question': row['question'],
                'answer': row['answer'],
                'create_dt': row['create_dt'],
                'update_dt': row['update_dt'], }

    @staticmethod
    async def all_data() -> Optional[List]:
        """
        Получение всех записей коллекции. (вопрос-ответ).

        :return: list(dict):
        """

        if db.faq is not None:
            rows = [FAQ.item(row) async for row in db.faq.find()]
        else:
            rows = []
        # async for row in db.faq.find():
        #     rows.append(FAQ.item(row))
        return rows

    @staticmethod
    async def all_questions() -> Optional[List]:
        """
        Получение всех вопрос из коллекции.

        :return: list(dict):
        """
        # rows = [
        #     {'id': row['_id'].__str__(),
        #      'question': row['question'],
        #      'update_dt': row['update_dt']} async for row in db.faq.find()]
        rows = [FAQ.item(row) async for row in db.faq.find()]
        return rows

    @staticmethod
    async def get_qa_from_id(_id: PyObjectId) -> Optional[Dict or None]:
        """
        Полученин одной записи вопрос-ответ по ее _id.

        :param _id: PyObjectId(str): индификатор записи
        :return: dict or None
        """
        row = await db.faq.find_one({"_id": PyObjectId(_id)})
        data = FAQ.item(row) if row is not None else None
        return data

    @staticmethod
    async def create_qa(payload: dict) -> Optional[bool or None]:
        """
        Создание новой записи в колекцию.

        :param payload: dict: входные данные
        :return: new_id: str: индификатор добавленой записи
        """
        now_ = now_dt()
        payload.update({'create_dt': now_, 'update_dt': now_})
        new_row = await db.faq.insert_one(payload)
        row = await db.faq.find_one({"_id": new_row.inserted_id})
        new_id = str(new_row.inserted_id) if row is not None else None
        logger.debug(f'Создана новая запись с _id=[{new_id}]')
        return new_id

    @staticmethod
    async def update_qa(_id: PyObjectId, payload: dict) -> Optional[bool or None]:
        """
        Обновление существующей записи, по ее _id.

        :param _id: PyObjectId(str): индификатор записи
        :param payload: dict: обновляемые данные
        :return: bool or None: результат выполнения
        """

        row = await db.faq.find_one({"_id": PyObjectId(_id)})
        if row is None:
            return None

        des_body = {k: v for k, v in payload.items() if v is not None}
        des_body.update({'update_dt': now_dt()})
        update_query = {"$set": {field: value for field, value in des_body.items()}}

        row = await db.faq.update_one({"_id": PyObjectId(_id)}, update_query)
        if row.modified_count == 1:
            logger.debug(f'Обновление объекта с id=[{_id}]')
            return True
        return False

    @staticmethod
    async def delete_qa(_id: PyObjectId) -> Optional[bool or None]:
        """
        Удаление записи из коллекции по _id.

        :param _id: PyObjectId(str): индификатор записи
        :return: bool or None: результат выполнения
        """
        row = await db.faq.find_one({"_id": PyObjectId(_id)})
        if row is None:
            return None

        row = await db.faq.delete_one({"_id": PyObjectId(_id)})
        if row.deleted_count == 1:
            logger.debug(f'Удаление объекта с id=[{_id}]')
            return True
        return False
