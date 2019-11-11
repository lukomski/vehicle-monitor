FROM python:3

WORKDIR /code
COPY . /code
RUN \
    pip install -r requirements.txt && \
    python manage.py makemigrations && \
    python manage.py migrate && \
    python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin', '', 'admin')" 
EXPOSE 8000
ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]
