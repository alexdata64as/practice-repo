"""
Модуль калькулятора для практики Git/GitHub
Теперь в структурированной папке src/
"""

def add(a: float, b: float) -> float:
    """Сложение двух чисел"""
    return a + b

def subtract(a: float, b: float) -> float:
    """Вычитание"""
    return a - b

def multiply(a: float, b: float) -> float:
    """Умножение"""
    return a * b

def divide(a: float, b: float) -> float:
    """Деление с проверкой на ноль"""
    if b == 0:
        raise ValueError("Деление на ноль!")
    return a / b

def power(a: float, b: float) -> float:
    """Возведение в степень"""
    return a ** b

def calculator_demo():
    """Демонстрация работы калькулятора"""
    print("Демонстрация калькулятора из структурированного проекта:")
    print(f"add(10, 5) = {add(10, 5)}")
    print(f"multiply(3, 4) = {multiply(3, 4)}")
    print(f"power(2, 3) = {power(2, 3)}")

if __name__ == "__main__":
    calculator_demo()
