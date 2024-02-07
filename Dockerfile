FROM python:3.11.4-slim-buster
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN mkdir /ceramic
WORKDIR /ceramic
RUN pip install --upgrade pip
RUN pip install django==4.2
RUN pip install djangoajax
RUN apt update -y
RUN apt install vim -y
COPY ./web /web/
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

