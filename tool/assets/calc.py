def plus(a, b):
    """Возвращает сумму a и b."""
    return a + b

def minus(a, b):
    """Возвращает разность a и b."""
    return a - b

def umnojenie(a, b):
    """Возвращает произведение a и b."""
    return a * b

def delenie(a, b):
    """Возвращает частное a и b, если b не равно 0. Иначе возвращает ошибку."""
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