#!/bin/sh

exec uvicorn app.app:api --host 0.0.0.0 --port 5000 --reload --log-config config/log.ini

