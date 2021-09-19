
FROM python:3.9-alpine

RUN mkdir /root/app

COPY ./app /root/app

WORKDIR /root/app

CMD ["python","Quiz.py"]
