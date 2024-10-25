def plus(a, b):
    return a + b

def minus(a, b):
    return a - b

def umnojenie(a, b):
    return a * b

def delenie(a, b):
    if b == 0:
        return "Ошибка: деление на ноль!"
    return a / b

def perform_operation(action, a, b):
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
