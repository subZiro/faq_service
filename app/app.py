"""
init application.
"""

import os

from app.api import home, faq
from app.api.auth import authorization
from app.common import create_application

print(os.getenv('FASTAPI_ENV'))
api, conf = create_application(os.getenv('FASTAPI_ENV', 'default'))

api.include_router(home, tags=["Main"], prefix='/home', dependencies=authorization)
api.include_router(faq, tags=["FAQ"], prefix='/', dependencies=authorization)
