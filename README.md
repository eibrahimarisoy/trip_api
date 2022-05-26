# Trip API

This repository contains Trip API written by Python/Django. It is a RESTful API.
Authentication is done using JWT. It is a JSON Web Token.
System has access and refresh tokens. 
The tokens validation time can be configured in the environment variables.

Anonymous user can only register and login the app.

Authenticated user can;
 - create, update, delete, and get her/his trips.
 - update her/his profile.
 - change her/his password.

## Using Tools
 - Django
 - Django Rest Framework
 - Django Geos API
 - Celery
 - JWT
 - PostgreSQL
 - Redis
 - Rest Framework Swagger
 - Virtualenv


## Dependencies used in the project
 - Python 3.7.2  
 - Postgres 14.2 follow the instructions [here](https://www.postgresql.org/download/)
 - Redis follow the instructions [here](https://redis.io/docs/getting-started/installation/install-redis-on-linux/)
 - Virtualenv you can follow the instructions [here](https://gist.github.com/Geoyi/d9fab4f609e9f75941946be45000632b)
 - PostGIS you can follow the instructions [here](https://computingforgeeks.com/how-to-install-postgis-on-ubuntu-linux/)

## Clone the project
```
$ git clone https://github.com/eibrahimarisoy/trip_api.git
$ virtualenv venv
$ source venv/bin/activate
$ cd trip_api
$ pip install -r requirements.txt
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py createsuperuser
```

## Configuration
App uses environment variables to configure the project.
You can edit file `.env` in the project pkg/config directory.
There is a sample file `.example.env` in the project directory.


## Run the project
```
$ python manage.py runserver
$ celery -A trip_api worker -l info
```

## Run the project with swagger

```
$ localhost:8000/api/v1/swagger/
```


## Contact

If you want to contact me you can reach me at <eibrahimarisoy@gmail.com>.