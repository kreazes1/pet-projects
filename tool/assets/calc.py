def plus(a, b):
    """Плюс a и b."""
    return a + b

def minus(a, b):
    """Минус a и b."""
    return a - b

def umnojenie(a, b):
    """Умножение a и b."""
    return a * b

def delenie(a, b):
    """Деление"""
    if b == 0:
        return "Ошибка: деление на ноль!"
    return a / b

def perform_operation(action, a, b):
    """Выполняет операцию в зависимости от действия."""
    if action == "1":
        return delenie(a, b)
    elif action == "2":
        return umnojenie(a, b)
    elif action == "3":
        return plus(a, b)
    elif action == "4":
        return minus(a, b)
    else:
        return "Ошибка: неверное действие."
