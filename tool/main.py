# Fore.GREEN + - Успешное выполнение
# Fore.RED + - Ошибка
# Fore.YELLOW + - Инпут
# Fore.WHITE(дефолт) - Выбор пункта 
#  + Style.RESET_ALL

import time
from colorama import Fore, Style
from assets import calc
from assets import admin_panel

print("""
██╗░░██╗██████╗░███████╗░█████╗░███████╗███████╗░██████╗
██║░██╔╝██╔══██╗██╔════╝██╔══██╗╚════██║██╔════╝██╔════╝
█████═╝░██████╔╝█████╗░░███████║░░███╔═╝█████╗░░╚█████╗░
██╔═██╗░██╔══██╗██╔══╝░░██╔══██║██╔══╝░░██╔══╝░░░╚═══██╗
██║░╚██╗██║░░██║███████╗██║░░██║███████╗███████╗██████╔╝
╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚══════╝╚══════╝╚═════╝░
                [Made by: kreazes.dev]
""")
print("""
1. Calculator \n
99. Войти в панель администратора
""")

select = input("Выберите один из пунктов выше: ")
if select == "1":
    first_number = int(input(Fore.YELLOW + "Введите первое число: "))
    second_number = int(input("Введите второе число: "))
    action = input("Выберите действие(1. Деление. 2. Умножение. 3. Плюс. 4. Минус): " + Style.RESET_ALL)

    result = calc.perform_operation(action, first_number, second_number)
    print(Fore.GREEN, f"Результат: {result}" + Style.RESET_ALL)

elif select == "99":
    admin_panel.admin_panel_logic()

else:
    print(Fore.RED + "Ошибка: неверное действие." + Style.RESET_ALL)