# Yatube
## Описание
API для создания публикаций, добавления к ним комментариев и c подпиской на других пользователей

## Как запустить проект
### Клонировать репозиторий и перейти в него в командной строке:
git clone https://github.com/FirstArchont/api-final-yatube-ad


cd yatube_api
### Cоздать и активировать виртуальное окружение:
python3 -m venv env


source env/bin/activate


### Установить зависимости из файла requirements.txt:
python3 -m pip install --upgrade pip


pip install -r requirements.txt


### Выполнить миграции:
python3 manage.py migrate
### Запустить проект:
python3 manage.py runserver

## Примеры запросов к API
### Создание поста
http://127.0.0.1:8000/api/v1/posts/


{
"text": "string",
"image": "string",
"group": 0
}
### Добавление комментария
http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/


{
  "text": "string"
}
### Продписка на пользователя
http://127.0.0.1:8000/api/v1/follow/


{
  "following": "string"
}
### Получение списка сообществ
http://127.0.0.1:8000/api/v1/groups/
