# Django MultiAdmin Project

Проект с несколькими административными панелями на Django.

## Особенности

- Несколько отдельных админ-панелей
- Разные права доступа для разных групп пользователей
- Основано на Django Unfold Admin

## Установка

1. Клонируйте репозиторий:
```bash
git clone https://github.com/genrihverter/django_multiadmin.git
```

2. Установите зависимости:
```bash
pip install -r requirements.txt
```

3. Настройте базу данных и примените миграции:
```bash
python manage.py migrate
```

4. Создайте суперпользователя:
```bash
python manage.py createsuperuser
```

5. Запустите сервер:
```bash
python manage.py runserver
```

## Доступные админки

- Основная админка: `/admin/`
- Админка 1: `/admin1/`
- Админка 2: `/admin2/`
