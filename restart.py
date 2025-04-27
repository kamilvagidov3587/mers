#!/usr/bin/env python3
"""
Скрипт для перезапуска приложения на Beget
"""

import os
import time

def restart_app():
    """Перезапуск приложения путем создания/обновления файла tmp/restart.txt"""
    
    # Создаем директорию tmp, если она не существует
    if not os.path.exists('tmp'):
        os.makedirs('tmp')
        print("Создана директория tmp")
    
    # Создаем или обновляем файл restart.txt
    restart_file = 'tmp/restart.txt'
    with open(restart_file, 'w') as f:
        f.write(f"Restart triggered at {time.strftime('%Y-%m-%d %H:%M:%S')}")
    
    print(f"Файл {restart_file} создан/обновлен")
    print("Приложение будет перезапущено в течение нескольких секунд")

if __name__ == '__main__':
    print("Перезапуск приложения на Beget...")
    restart_app()
    print("Готово! Теперь обновите страницу в браузере.") 