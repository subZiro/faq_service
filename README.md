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
