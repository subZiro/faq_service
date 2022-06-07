"""
init application.
"""

import os

from app.api import home, faq
from app.api.auth import authorization
from app.common import create_application
from app.database import db

api, conf = create_application(os.getenv('FASTAPI_ENV', 'default'))


@api.on_event("startup")
async def startup():
    await db.connect_to_database(path=conf.DATABASE_URL,
                                 database=conf.DATABASE_NAME,
                                 collections_name=conf.COLLECTION)


@api.on_event("shutdown")
async def shutdown():
    await db.close_database_connection()


api.include_router(home, tags=["Main"], prefix='/home', dependencies=authorization)
api.include_router(faq, tags=["FAQ"], prefix='/', dependencies=authorization)
