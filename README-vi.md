![](https://img.shields.io/github/license/tinnguyentg/dictionaries-django-web-application?style=plastic)
![](https://img.shields.io/github/last-commit/tinnguyentg/dictionaries-django-web-application)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# Ứng dụng web Từ điển cá nhân

Ứng dụng web tra cứu, lưu trữ từ vựng sử dụng Django framework. Dữ liệu từ điển từ Oxford Dictionaries API.

## Screenshots

![index](/screenshots/Screenshot-index.png)
![detail](/screenshots/Screenshot-detail.png)

## Cài đặt

- Cần có [Oxford Dictionaries API credentials](https://developer.oxforddictionaries.com/credentials)
- Chỉnh sửa 2 biến `OXFORD_APP_ID`, `OXFORD_APP_KEY` ở `project/settings/base.py`.
- Sau đó sử dụng như một dự án Django thông thường
```shell

pip install -r requirements/dev.txt

python manage.py migrate
python manage.py runserver
```

## Sử dụng Docker

- Sao chép tệp `.env.example` thành `.env`
- Chỉnh sửa giá trị của các biến trong file `.env`
- Sử dụng `docker compose`
```shell
docker compose up -d
docker compose exec django python manage.py migrate
docker compose exec django python manage.py collectstatic
```

## Chỉnh sửa

Fork repo này, thêm các chức năng hoặc chỉnh sửa giao diện như bạn mong muốn 😄😄😄😄


------

![](https://languages.oup.com/wp-content/uploads/ol-logo-colour-300px-sfw.jpg)