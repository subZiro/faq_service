"""
Create application.
"""

from datetime import datetime
from typing import ClassVar, Optional

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app import logger
from config.config import config, Config


logger = logger.getChild('common')



async def str_to_dt(value: str) -> Optional[datetime or None]:
    """"""
    try:
        result = datetime.strptime(value, Config.DT_TMPL)
    except ValueError as err:
        result = None
        logger.debug(f'Ошибка формата даты окончания токена. ERROR=[{err}]')
    return result


def now_dt():
    """
    Получение datetime.now в зафиксированном формате.

    :return:
    """
    return datetime.now().strftime(Config.DT_TMPL)


def get_config(conf_name: str) -> ClassVar:
    """
    Получение настроек приложения.

    :return: ClassVar: класс конфигурации
    """
    # conf_name = os.getenv('FASTAPI_CONFIG', 'default')

    if conf_name == 'default':
        logger.warning('Не найден конфигурационный файл.')
    logger.debug(f'Выполнена загрузка [{conf_name}] конфигурации')
    return config[conf_name]


def create_application(conf_name: str) -> tuple:
    """
    Создание приложения.

    :param conf_name: str:
    :return app, config: tuple(FastApi, ClassVar):
    """

    app_conf = get_config(conf_name)
    app = FastAPI(title=f'FAQ for SNEG Aqualife. {app_conf.ENV} stage',
                  description='backend FastAPI, database MongoDB',
                  version=app_conf.VERSION,
                  debug=app_conf.DEBUG,
                  docs_url=app_conf.DOCS_URL,
                  redoc_url=app_conf.REDOC_URL,
                  root_path=app_conf.ROOT_PATH,
                  root_path_in_servers=app_conf.ROOT_PATH_IN_SRV,
                  )

    app.add_middleware(CORSMiddleware,
                       allow_origins=['*'],
                       allow_credentials=True,
                       allow_methods=[""],
                       allow_headers=["*"])
    logger.debug('Создано FastApi приложение.')
    return app, app_conf
