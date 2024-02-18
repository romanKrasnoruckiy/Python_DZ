from Python_DZ.choice_file import choice_number_file
from support_func import read_data_file


def data_file():
    nf = choice_number_file()
    data = read_data_file(nf)
    return data, nf