import colorama
from colorama import Fore, Style
import json
import os

colorama.init()

def load_admin_password():
    password_file = 'admin_key.json'
    if not os.path.exists(password_file):
        with open(password_file, 'w') as file:
            json.dump({'password': 'admin'}, file)
        return 'admin'

    with open(password_file, 'r') as file:
        data = json.load(file)
    return data['password']

def change_password(new_password):
    password_file = 'admin_key.json'

    with open(password_file, 'r') as file:
        data = json.load(file)

    data['password'] = new_password

    with open(password_file, 'w') as file:
        json.dump(data, file)

def admin_panel_logic():
    admin_password = load_admin_password()
    input_key = input(Fore.YELLOW + "Введите пароль для входа в админ-панель: " + Style.RESET_ALL)
    
    if input_key == admin_password:
        print(Fore.GREEN + """
Добро пожаловать, администратор! Выберите один из пунктов ниже!\n
1. Изменить пароль для входа в админ-панель\n
2. Добавить пункты на главную страницу
""" + Style.RESET_ALL)
        admin_select = input(Fore.YELLOW + "Ваш ответ: " + Style.RESET_ALL)
        if admin_select == "1":
            admin_password_select = input(Fore.YELLOW + "Введите новый пароль: " + Style.RESET_ALL)
            change_password(admin_password_select)
            print(Fore.GREEN, f"Успешно! Новый пароль: {admin_password_select}" + Style.RESET_ALL)
        elif admin_select == "2":
            print(Fore.RED + "Ошибка: Данная функция еще не реализована." + Style.RESET_ALL)
    else:
        print(Fore.RED + "Ошибка: неверный пароль." + Style.RESET_ALL)