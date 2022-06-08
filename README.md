# faq_service

Frequently asked Questions service. FastApi-RESTPlus, Swagger UI doc, MongoDB.

----


### краткая инструкция по развертыванию:
##### Установка окружения
```
+ перейти в директорию, содержащую файл requirements.txt
+ создать виртуальное окружение:
    python3 -m venv venv
+ активировать виртуальное окружение:
    source venv/bin/activate
+ установить необходимые зависимости:
    pip3 install -r requirements.txt
+ задать переменные окружения
    DATABASE_URL='ваш адрес mongodb'
+ запустить приложение:
    1. sh ./sh/boot.sh
    2. python3 main.py
проект доступен в по адресу http://localhost:5000/docs/
```

### краткая инструкция по развертыванию с docker-compose:
```
+ задать переменные окружения
    DB_USER=пользователь бд
    DB_PASSWORD=пароль бд
    DB_NAME=имя бд
    API_TOKEN=токен авторизации к апи
    'export ПЕРЕМЕННАЯ=ЗНАЧЕНИЕ'
+ перейти в директорию, содержащую файл main.py
+ выболнить сборку проекта:
'docker-compose -f docker-compose.yml build --parallel'
+ выполнить запуск проекта 
'docker-compose -f docker-compose.yml up -d'

проект доступен в по адресу http://localhost:5000/docs/
```