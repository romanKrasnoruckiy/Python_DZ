def nf_row_input(count_rows):
    number_row = int(input(f"Введите номер строки "
                               f"от 1 до {count_rows}: "))
    while number_row < 1 or number_row > count_rows:
        number_row = int(input(f"Ошибка!"
                                f"Введите номер строки "
                                f"от 1 до {count_rows}: "))
    return number_row

def num_row_change(data):
    data = [f'{i + 1};{data[i].split(";")[1]};'
                f'{data[i].split(";")[2]};'
                f'{data[i].split(";")[3]};'
                f'{data[i].split(";")[4]}'
                for i in range(len(data))]
    return data

def read_data_file(nf):
    with open(f'db/data_{nf}.txt', 'r', encoding='utf-8') as file:
        data = file.readlines()
    return data

def exit():
    print("Спасибо, что воспользовались нашими услугами!\n"
        "Всего доброго! Приходите к нам ещё :)")
    return True

def data_write(nf, data):
    with open(f'db/data_{nf}.txt', 'w', encoding='utf-8') as file:
        file.writelines(data) 