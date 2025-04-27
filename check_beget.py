#!/usr/bin/env python3
"""
Скрипт для проверки работоспособности приложения на хостинге Beget
"""

import os
import sys
import json

def check_environment():
    """Проверка окружения"""
    print("Проверка окружения Python...")
    print(f"Python версия: {sys.version}")
    print(f"Путь к Python: {sys.executable}")
    print(f"Текущая директория: {os.getcwd()}")
    
    # Проверка наличия необходимых директорий
    required_dirs = ['templates', 'static', 'data']
    for d in required_dirs:
        if os.path.exists(d) and os.path.isdir(d):
            print(f"✓ Директория {d} существует")
        else:
            print(f"✗ Директория {d} не найдена!")
    
    # Проверка наличия необходимых файлов
    required_files = ['app.py', 'passenger_wsgi.py', '.htaccess', 'requirements.txt']
    for f in required_files:
        if os.path.exists(f) and os.path.isfile(f):
            print(f"✓ Файл {f} существует")
        else:
            print(f"✗ Файл {f} не найден!")
    
    # Проверка разрешений на запись для директории data
    if os.path.exists('data'):
        try:
            test_file = 'data/test_write.tmp'
            with open(test_file, 'w') as f:
                f.write('test')
            os.remove(test_file)
            print("✓ Директория data доступна для записи")
        except Exception as e:
            print(f"✗ Ошибка записи в директорию data: {e}")
    
    # Проверка settings.json
    if os.path.exists('settings.json'):
        try:
            with open('settings.json', 'r', encoding='utf-8') as f:
                settings = json.load(f)
            print("✓ Файл settings.json прочитан успешно")
            
            # Проверка Яндекс токена
            if 'backup_settings' in settings and 'yandex_token' in settings['backup_settings']:
                token = settings['backup_settings']['yandex_token']
                if token:
                    print(f"✓ Токен Яндекс.Диска настроен: {token[:5]}...{token[-5:]}")
                else:
                    print("✗ Токен Яндекс.Диска не задан")
            else:
                print("✗ Настройки резервного копирования не найдены")
        except Exception as e:
            print(f"✗ Ошибка чтения settings.json: {e}")
    else:
        print("✗ Файл settings.json не найден")
    
def main():
    """Основная функция проверки"""
    print("=" * 50)
    print("ПРОВЕРКА РАБОТОСПОСОБНОСТИ ПРИЛОЖЕНИЯ НА BEGET")
    print("=" * 50)
    
    check_environment()
    
    print("\nПроверка импорта модулей Flask...")
    try:
        import flask
        print(f"✓ Flask установлен (версия {flask.__version__})")
    except ImportError:
        print("✗ Flask не установлен!")
    
    try:
        import xlsxwriter
        print("✓ XlsxWriter установлен")
    except ImportError:
        print("✗ XlsxWriter не установлен!")
    
    try:
        import requests
        print("✓ Requests установлен")
    except ImportError:
        print("✗ Requests не установлен!")
    
    print("\nПроверка создания тестового приложения Flask...")
    try:
        from flask import Flask
        test_app = Flask(__name__)
        print("✓ Тестовое приложение Flask создано успешно")
    except Exception as e:
        print(f"✗ Ошибка создания тестового приложения Flask: {e}")
    
    print("\nПроверка импорта основного приложения...")
    try:
        from app import app
        print("✓ Импорт основного приложения выполнен успешно")
    except Exception as e:
        print(f"✗ Ошибка импорта основного приложения: {e}")
    
    print("\nРезультаты проверки:")
    print("1. Для полной проверки работоспособности перейдите по адресу вашего сайта")
    print("2. Если видите ошибку 502, проверьте пути в passenger_wsgi.py")
    print("3. Убедитесь, что все необходимые зависимости установлены")
    print("4. Перезапустите приложение: touch tmp/restart.txt")
    print("\nЕсли все проверки выполнены успешно, ваше приложение должно работать на Beget!")

if __name__ == "__main__":
    main() 