#!/usr/bin/env python3
"""
Файл конфигурации для запуска Flask-приложения на хостинге Beget
"""

import sys
import os

# Добавляем путь к текущей директории в Python path
INTERP = os.path.expanduser("/home/u/user/path/to/venv/bin/python3")
if sys.executable != INTERP:
    os.execl(INTERP, INTERP, *sys.argv)

sys.path.append(os.getcwd())

# Импортируем приложение Flask из нашего файла app.py
from app import app as application

# Для корректной работы на Beget
application.secret_key = os.getenv('SECRET_KEY', 'secret_key_for_session') 