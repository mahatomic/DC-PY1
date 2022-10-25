def get_count_char(str_):
    dict_char = {}
    for char in str_.lower():
        if char.isalpha():
            if char in dict_char:
                dict_char[char] += 1
            else:
                dict_char[char] = 1
    return dict_char

def char_in_proc(dict_):
    SUM_VALUES = sum(dict_.values())
    PROC = 100  # константа для перевода в проценты
    for value in dict_:
        dict_[value] = round((dict_[value] * PROC / SUM_VALUES), 2)
    return dict_

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
print(char_in_proc(get_count_char(main_str)))
