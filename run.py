#!/usr/bin/env python3
"""
Точка входа для запуска проекта из корневой директории
"""

import sys
import os

# Добавляем src в путь
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

try:
    from main import main
    main()
except ImportError as e:
    print(f"Ошибка импорта: {e}")
    print("Убедитесь что:")
    print("1. Вы находитесь в корне проекта")
    print("2. Папка src/ существует")
    print("3. main.py находится в src/")
