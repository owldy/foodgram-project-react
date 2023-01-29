![example workflow](https://github.com/owldy/foodgram-project-react/actions/workflows/foodgram_workflow.yaml/badge.svg)

## Описание проекта

Foodgram - сервис для публикации, поиска и выбора кулинарных рецептов. Каждый может авторизоваться, выложить свои рецепты, подписаться на других пользователей, добавлять
рецепты в избранное или в список покупок, скачать список покупок.

## Где посмотреть развернутый проект

Проект развернут по адресу: http://localhost:8000/signin
Админка: http://localhost:8000/admin/

## Инструкция по запуску проекта

Для запуска проекта необходимо создать папку infra, поместить в нее файлы .env, docker-compose.yml и nginx.conf

По порядку выполнить следующие команды:

- git clone 
- foodgram-project-react.git
- cd infra
- docker-compose up -d --build
- docker container ls (скоровать id контейнера бэкенда)
- docker exec -it 'id контейнера' bash
- python manage.py makemigrations app
- python manage.py migrate
- python manage.py createsuperuser
- python manage.py collectstatic --no-input
- python manage.py importcsv (данные для загрузки уже лежат в проекте)

## Документация проекта

Документация проекта доступна по адресу: 
http://localhost:8000/api/docs/
