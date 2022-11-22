def get_count_char(str_):
    dict_char = {}
    for char in str_.lower():
        if char.isalpha():
            dict_char[char] = dict_char.get(char, 0) + 1
    return dict_char

def char_in_proc(dict_):
    new_dict = dict_.copy()
    sum_values = sum(new_dict.values())
    for value in new_dict:
        new_dict[value] = round((new_dict[value] * 100 / sum_values), 2)
    return new_dict

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
print(char_in_proc(get_count_char(main_str)))
