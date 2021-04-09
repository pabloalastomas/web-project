FROM python:latest
RUN mkdir /app
WORKDIR /app
ADD requirements.txt /app/
RUN pip install -r requirements.txt
ADD . /app/
RUN cd /app && python manage.py migrate
