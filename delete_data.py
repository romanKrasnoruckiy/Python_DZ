from return_data_file import data_file
from support_func import nf_row_input
from support_func import num_row_change
from support_func import data_write

def delete_row(data = None, nf = None, number_row = None):
    if data == None and nf == None:
        data, nf = data_file()
    count_rows = len(data)
    if count_rows == 0:
        print("Файл пустой!")
    else:
        if number_row == None:
            number_row = nf_row_input(count_rows)
        del data[number_row - 1]
        data = num_row_change(data)
        data_write(nf, data)
        print("Строка успешно удалена!")