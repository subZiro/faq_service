"""
init application.
"""

import os

from app.api import home
from app.common import create_application

print(os.getenv('FASTAPI_ENV'))
api, conf = create_application(os.getenv('FASTAPI_ENV', 'default'))

api.include_router(home, tags=["Main"], prefix='/home', dependencies=authorization)
