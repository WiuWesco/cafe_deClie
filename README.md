# Кафе "de_clie"

Проект "de_clie" - это веб-приложение, созданное в рамках учебного курса в 9 классе. Сайт предоставляет пользователям возможность ознакомиться с ассортиментом и атмосферой кафе "de_clie" и, при желании, забронировать столик. Администратор может редактировать содержимое сайта через админ-панель.

## Технологии

- Backend: Django
- Frontend: UI Kit

## Функциональность

- Просмотр меню кафе с описанием блюд и ценами.
- Просмотр информации о кафе, такой как адрес, контактная информация, часы работы и т.д.
- Возможность онлайн-бронирования столиков для посещения кафе.
- Администраторская панель для редактирования контента сайта.

## Установка и запуск

1. Клонируйте репозиторий: `git clone https://github.com/ваш-логин/de_clie.git`
2. Перейдите в папку с проектом: `cd de_clie`
3. Установите зависимости: `pip install -r requirements.txt`
4. Примените миграции: `python manage.py migrate`
5. Создайте суперпользователя: `python manage.py createsuperuser`
6. Запустите сервер: `python manage.py runserver`
7. Откройте веб-браузер и перейдите по адресу `http://127.0.0.1:8000/`
