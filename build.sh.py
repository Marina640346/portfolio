#!/usr/bin/env bash
# Exit on error
set -o errexit

# Встановлюємо залежності
pip install -r requirements.txt

# Збираємо статичні файли (CSS, JS, картинки)
python manage.py collectstatic --no-input

# Виконуємо міграції бази даних
python manage.py migrate