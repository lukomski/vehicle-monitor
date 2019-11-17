# vehicle-monitor

RUN project

`docker-compose up --build`

* be patient it takes a few minutes

------------------------------
Old Run project:

`docker build -t vehicle_monitor:v1 .  `

`docker run -it -p 8000:8000 --rm vehicle_monitor:v1`

URLs:

* lpr/  -   ''
* lpr/plate_reader  -   runs plate recognizing function with given image
* lpr/all   -   all occurences of license plates
* lpr/present   -   occurences with exit time = null
* lpr/[license plate]/details   -   occurences of car with given [license plate]
* lpr/new   -   actualize state of database, based on photo with license plates

