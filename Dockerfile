FROM python:3

WORKDIR /code
COPY . /code
RUN \
    pip install -r requirements.txt && \
    python manage.py makemigrations && \
    python manage.py migrate && \
    python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin', '', 'admin')"

RUN apt update 
RUN apt install -y software-properties-common
RUN add-apt-repository -y ppa:alex-p/tesseract-ocr
RUN apt install -y tesseract-ocr
RUN apt install -y openalpr openalpr-daemon openalpr-utils libopenalpr-dev vim
RUN ln -s /usr/share/openalpr/runtime_data/ocr/tessdata/lus.traineddata /usr/share/openalpr/runtime_data/ocr/lus.traineddata

EXPOSE 8000
CMD python manage.py test; python manage.py runserver 0.0.0.0:8000