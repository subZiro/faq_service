FROM tiangolo/uvicorn-gunicorn:python3.9-alpine3.14

ENV PYTHONPATH=/home/faq TZ=Europe/Moscow

RUN adduser -D faq
WORKDIR /home/faq

COPY requirements.txt requirements.txt
RUN apk update && \
    apk upgrade && \
    pip3 install --upgrade pip && \
    python3 -m pip install -r requirements.txt --no-cache-dir

COPY app app
COPY sh sh
# COPY tests tests
COPY config.py log.ini pytest.ini main.py ./

RUN mkdir temp && \
    chown -R faq:faq *
USER faq
