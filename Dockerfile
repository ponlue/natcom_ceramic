FROM python:3.11.4-slim-buster
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN mkdir /ceramic
WORKDIR /ceramic
RUN pip install --upgrade pip
RUN pip install django==4.2
RUN pip install djangoajax
RUN pip install  django-simple-captcha 
RUN pip install django-multi-captcha-admin
RUN pip install django-ckeditor
RUN apt update -y
RUN apt install vim -y
COPY . /ceramic/
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

