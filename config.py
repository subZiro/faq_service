import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    """
    Базовый конфигурационный класс приложения
    """

    VERSION = '0.1.1'
    DEBUG = True
    ROOT_PATH = ''
    DOCS_URL = '/docs/'
    REDOC_URL = '/redoc/'
    ROOT_PATH_IN_SRV = True

    BASE_URL = 'http://localhost:5000'
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    API_TOKEN = os.environ.get('API_TOKEN')

    DATABASE_URL = os.environ.get('DATABASE_URL')
    DATABASE_NAME = os.environ.get('DB_NAME')
    COLLECTION = ['faq_collection',]

    DATE_TMPL = '%Y-%m-%d'
    DT_TMPL = "%Y-%m-%dT%H:%M:%S"

    BASEDIR = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir))
    LOG_FILE = f'{BASEDIR}/temp/log.log'
    LOG_CFG = f'{BASEDIR}/config/log.ini'

    BASE_URL = 'http://testserver'
