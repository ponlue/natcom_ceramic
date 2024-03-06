FROM python:3.11.4-slim-buster
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN mkdir /ceramic
WORKDIR /ceramic
RUN pip install --upgrade pip
RUN pip install django==4.2
RUN pip install mysql-connector-python==8.3.0
RUN pip install django-multi-captcha-admin
RUN pip install django-ckeditor
RUN pip install django-recaptcha==4.0.0
RUN pip install django-ckeditor-5
RUN apt-get update -y
RUN apt install vim -y
COPY . .
EXPOSE 9999
CMD ["python", "manage.py", "makemigrations"]
CMD ["python","manage.py","migrate"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:9999"]
