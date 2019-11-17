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
RUN wget https://techsat24.pl/img/product_media/32001-33000/Samochod-na-akumulator-BMW-X6M-Niebieski-Lakier-Metalik-PILOT-132189.jpg
RUN mv Samochod-na-akumulator-BMW-X6M-Niebieski-Lakier-Metalik-PILOT-132189.jpg samochod.jgp
RUN wget http://plates.openalpr.com/h786poj.jpg

EXPOSE 8000
ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]
