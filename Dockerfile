FROM python:3.9-alpine
COPY . /app
WORKDIR /app/myproject
RUN pip install -r ../requirements.txt

EXPOSE 8000
CMD ["python", "manage.py","runserver","0.0.0.0:8000"]

