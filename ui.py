from Python_DZ.delete_data import delete_row
from Python_DZ.change_data import change_row
from Python_DZ.add_data import add_row
from print_data import print_file
from Python_DZ.copy_data import copy_row
from support_func import exit

def menu_read():
    with open(f'menu.txt', 'r', encoding='utf-8') as file:
        data = file.readlines()
    menu = {}
    for line in data:
        key, name, value = line.strip().split(';')
        menu[key] = [name, value]
    return menu

def start_menu():
    menu = menu_read()
    command = False
    menu_str = [f"{key}. {menu[key][0]}" for key in menu]
    output_menu = '\n'.join(menu_str).lstrip(" ")
    print("Доброго времени суток!\n")
    while not command:
        print("Выберите функцию:\n",output_menu)
        command = input("Введите номер команды: ")
        if command not in menu.keys():
            print("Ошибка, такого номера команды не существует!")
            command = False
        else:
            name = menu[command][1] 
            command = globals()[name]()
