![](https://img.shields.io/github/license/tinnguyentg/dictionaries-django-web-application?style=plastic)
![](https://img.shields.io/github/last-commit/tinnguyentg/dictionaries-django-web-application)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# Dictionaries web application

Web application for searching, storing dictionary using Django framework, data from Oxford Dictionaries API.

## Screenshots

![index](/screenshots/Screenshot-index.png)
![detail](/screenshots/Screenshot-detail.png)


## Installation


- You need [Oxford Dictionaries API credentials](https://developer.oxforddictionaries.com/credentials)
- Edit `OXFORD_APP_ID`, `OXFORD_APP_KEY` at `project/settings/base.py`.
- Run django project

```shell

pip install -r requirements/dev.txt

python manage.py migrate
python manage.py runserver
```


## Using Docker

- Copy `.env.example` -> `.env`
- Edit `.env` file
- Run docker compose
```shell
docker compose up -d
docker compose exec django python manage.py migrate
docker compose exec django python manage.py collectstatic
```

## E

Fork this repo, feel free to add more features and styles as you wish 😄😄😄😄

------

![](https://languages.oup.com/wp-content/uploads/ol-logo-colour-300px-sfw.jpg)