from return_data_file import data_file
from support_func import nf_row_input
from support_func import num_row_change
from support_func import read_data_file
from Python_DZ.delete_data import delete_row
from support_func import data_write


def copy_row():
    data, nf = data_file()
    text = ""
    if len(data) == 0:
        print("Файл пустой!")
    else:
        nf_row = nf_row_input(len(data))
        confirm = ""
        while confirm.lower() != "д" and confirm.lower() !="н":
            confirm = input(f"Хотите удалить копируемую строку из файла {nf}? (д/н): ")
        if nf == 1:
            data_new = read_data_file(2)
            data_new.append(data[nf_row-1])
            data_new = num_row_change(data_new)
            data_write(2, data_new) 
        else:
            data_new = read_data_file(1)
            data_new.append(data[nf_row-1])
            data_new = num_row_change(data_new)
            delete_row(data, nf, nf_row)
            data_write(1, data_new)
        if confirm.lower() == "д":
            delete_row(data, nf, nf_row)
            text = f"Исходная строка из {nf} файла удалена."
        print(f"Данные успешно скопированы. {text}")