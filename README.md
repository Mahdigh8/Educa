# Educa
A simple CMS service created by Django
## Getting Started
* Before start you need to install python 3.x or later and virtualenv on your computer.
### Installation
1- Download project go to the directory and open a terminal in that directory.

2- Run the commands below:
```
$ virtualenv .venv --python=python3 && source .venv/bin/activate
```

```
$ pip install -r requirements.txt
```

```
$ python manage.py migrate
```

3- Now Run the the command below and create an admin user
```
$ python manage.py createsuperuser
```

4- Run the command below to run the server
```
$ redis-4.0.11/src/redis-server 
```
**redis is used to store the module id for each course that student enroll in to continue that course later from that module.**

5- And then in another terminal in this directory run the command below:
```
$ python manage.py runserver
```

Now open this url in your browser 127.0.0.1:8000

## Built With
* [Django](https://www.djangoproject.com/) - The web framework used
* [Bootstrap 4](https://getbootstrap.com/) - The frontend framework