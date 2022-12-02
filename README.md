# API_FINAL_YATUBE

### Описание проекта

Данный проект является api-сервисом для проекта [Yatube](https://github.com/Etozheigor/hw05_final).
Он дает пользователям возможность обращаться к проекту Yatube с различных устройств и сервисов и получать необходимый контент.
Yatube наполенен таким конетентом, как посты пользователей, комментарии к ним, тематические группы, подписки авторов друг на друга.


### Как запустить:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Etozheigor/api_final_yatube
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

```
source venv/Scripts/activate
```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```
### Примеры обращений к API Yatube

После запуска проекта вы можете обратиться к документации проекта по следующему адресу:

```
http://127.0.0.1:8000/redoc/
```
Там описаны все примеры обращений к сервису и его ответы.

## Да прибудет с вами API
![yoda](https://user-images.githubusercontent.com/104680302/185987811-ff9b852f-692a-405d-b9a7-e1a0db943d6f.png)


