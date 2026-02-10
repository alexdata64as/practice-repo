#!/usr/bin/env python3
"""
Минимальный тест для задания
"""

import os

# Попытка загрузить .env
try:
    from dotenv import load_dotenv
    load_dotenv()
    print(">>> .env загружен успешно")
except:
    print(">>> Не удалось загрузить .env")
    # Выходим если не установлена библиотека
    exit(1)

# Функция из задания
def print_author():
    # Допишите здесь ваш код
    author = os.getenv("AUTHOR")
    print(f"Автор проекта: {author}")

# Проверка
print(">>> Тестируем функцию print_author():")
print_author()
