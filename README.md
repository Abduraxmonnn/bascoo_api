## Welcome to
# Bascoo

### About the Project

soon...

### About the BackEnd

This project raised in architecture `MVT` `(Model View Template)`.

### About the FrontEnd
You can view project in github with link: soon...

***

## Tech

* [Django](https://www.djangoproject.com/) - is a high-level `Python Web framework`
* [Django REST framework](https://www.django-rest-framework.org/) - `Django REST Framework` is a powerful and flexible toolkit for building Web `APIs`
* [SQLite](https://www.sqlite.org/) - open source object-relational database system

And many other libraries.

Dillinger requires [Python](https://www.python.org) `v3.10+` or `v3.12`.

```shell
$ git clone https://github.com/Abduraxmonnn/bascoo_api.git
$ cd bascoo_api
```

***

## Setting project

* `Linux`
```shell
$ virtualenv -p /usr/bin/python3 .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
$ python manage.py migrate
```

* `Windows`
```shell
$ python -m venv ./venv
$ venv\Scripts\activate
$ pip install -r requirements.txt
$ python manage.py migrate
```

* `MacBook`
```shell
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ python manage.py migrate
```

***

## Development

Run the project.
```shell
$ python manage.py runserver
```
`Output`
```shell
System check identified no issues (0 silenced).
Month date, year - hh:mm:ss
Django version 4.1.7, using settings 'config.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```
Open http://127.0.0.1:8000 in your browser for see result.