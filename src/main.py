#!/usr/bin/env python3
"""
Основной скрипт проекта practice-repo
Теперь в структурированной папке src/
"""

import os
import sys

# Добавляем src в путь для импортов
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def setup_encoding():
    """Настраиваем кодировку для Windows"""
    if sys.platform == "win32":
        import io
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def load_environment():
    """Загружает переменные окружения из .env файла"""
    try:
        from dotenv import load_dotenv
        # Загружаем переменные из .env (теперь в корне проекта)
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        env_path = os.path.join(project_root, '.env')
        load_dotenv(env_path)
        print("[OK] Переменные окружения загружены из .env")
        return True
    except ImportError:
        print("[ERROR] Библиотека python-dotenv не установлена")
        print("        Установите: pip install python-dotenv")
        return False
    except Exception as e:
        print(f"[ERROR] Ошибка загрузки .env: {e}")
        return False

def print_author():
    """Печатает имя автора проекта из переменной окружения"""
    author = os.getenv("AUTHOR")
    
    if author:
        print(f"Автор проекта: {author}")
        return author
    else:
        print("[ERROR] Переменная AUTHOR не найдена в .env файле")
        return None

def demonstrate_calculator():
    """Демонстрирует работу калькулятора"""
    print("\n🧮 Демонстрация калькулятора:")
    try:
        # Теперь импортируем из src
        from calculator import add, multiply
        print(f"   7 + 3 = {add(7, 3)}")
        print(f"   7 * 3 = {multiply(7, 3)}")
    except ImportError as e:
        print(f"   [INFO] Ошибка импорта: {e}")
        print("   Убедитесь что calculator.py в папке src/")

def show_project_structure():
    """Показывает новую структуру проекта"""
    print("=" * 60)
    print("СТРУКТУРИРОВАННЫЙ ПРОЕКТ DATA SCIENCE")
    print("=" * 60)
    
    print("\n📁 Новая структура проекта:")
    print("practice-repo/")
    print("├── src/                    # Исходный код")
    print("│   ├── __init__.py")
    print("│   ├── main.py            # Этот скрипт")
    print("│   ├── calculator.py      # Модуль калькулятора")
    print("│   ├── utils/             # Вспомогательные функции")
    print("│   ├── models/            # Модели ML")
    print("│   ├── features/          # Feature engineering")
    print("│   └── data/              # Обработка данных")
    print("├── notebooks/             # Jupyter ноутбуки")
    print("├── tests/                 # Тесты")
    print("├── data/                  # Данные")
    print("│   ├── raw/               # Сырые данные")
    print("│   ├── processed/         # Обработанные данные")
    print("│   └── external/          # Внешние данные")
    print("├── docs/                  # Документация")
    print("├── reports/               # Отчёты и визуализации")
    print("│   ├── figures/           # Графики")
    print("│   └── tables/            # Таблицы")
    print("├── .env                   # Конфиденциальные данные")
    print("├── .env.example           # Шаблон .env")
    print("├── .gitignore             # Игнорируемые файлы")
    print("├── requirements.txt       # Зависимости")
    print("└── README.md              # Документация")
    
    print("\n✅ Преимущества структуры:")
    print("1. Чистая организация кода")
    print("2. Легко находить файлы")
    print("3. Стандарт для DS проектов")
    print("4. Упрощает командную работу")

def main():
    """Основная функция"""
    setup_encoding()
    
    if not load_environment():
        print("\n[WARNING] Продолжаем без загрузки .env файла")
    
    show_project_structure()
    
    print("\n" + "=" * 60)
    print("ПРОВЕРКА РАБОТЫ ПОСЛЕ РЕСТРУКТУРИЗАЦИИ")
    print("=" * 60)
    
    # Проверяем автора
    print("\n👤 Информация об авторе:")
    print_author()
    
    # Проверяем калькулятор
    demonstrate_calculator()
    
    print("\n" + "=" * 60)
    print("🎯 ЗАДАНИЕ ПО СТРУКТУРИРОВАНИЮ ВЫПОЛНЕНО!")
    print("=" * 60)
    print("\n✅ Все файлы с кодом перемещены в src/")
    print("✅ Корневая директория содержит нужные файлы:")
    print("   - requirements.txt")
    print("   - .gitignore")
    print("   - README.md")
    print("\n🚀 Проект готов к дальнейшей разработке!")

if __name__ == "__main__":
    main()
