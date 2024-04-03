# Movie-Rating-System
This is the completed backend component of the movie rating system application built with Python.

## Technology used
Python, Django, Django Rest Framework, and Postgresql as the database.

# Prerequisites
1. To run this project you need to install docker on your system.

# Installation
1. Clone the repository:
2. Change directory to movie_rating_system by running `cd movie_rating_system`
3. Set up following environment variables:

```
DEBUG=True
SECRET_KEY=14dgbfpj@@1@(-y4x2rub8b72x4h*o#^2zj!s5vqtn(s8l+yz1+oj=yi

DB_NAME=movie_system_db
DB_USER=postgres
DB_PASSWORD=123456
DB_HOST=host.docker.internal
DB_PORT=5430
```

Create a .env file in the root directory and provide the required values for environment variables such as database credentials.

# Build Docker containers:

```make docker-build ```

This command will build and start the Docker containers required for the project.

# Admin Interface:
The admin panel can be accessed at http://localhost:8000/admin/
But you need to create a superuser first.

# Create Super User
To visit the admin interface you need to create a superuser account from the docker cli
``` python manage.py createsuperuser ```
