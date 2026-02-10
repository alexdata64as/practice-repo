#!/usr/bin/env python3
"""
Простой тест для проверки работы с .env
Без Unicode символов для Windows
"""

import os

# Проверяем наличие библиотеки
try:
    from dotenv import load_dotenv
    print("[TEST] Библиотека python-dotenv найдена")
    
    # Загружаем .env
    load_dotenv()
    print("[TEST] .env файл загружен")
    
    # Проверяем переменную AUTHOR
    author = os.getenv("AUTHOR")
    if author:
        print(f"[TEST] Автор проекта: {author}")
        print("[TEST] ТЕСТ ПРОЙДЕН УСПЕШНО!")
    else:
        print("[TEST] ОШИБКА: Переменная AUTHOR не найдена")
        
except ImportError:
    print("[TEST] ОШИБКА: Библиотека python-dotenv не установлена")
    print("        Выполните: pip install python-dotenv")
    
except Exception as e:
    print(f"[TEST] ОШИБКА: {e}")
