def get_count_char(str_):
    dict_char = {}
    for char in str_.lower():
        if char.isalpha():
            dict_char[char] = dict_char.get(char, 0) + 1
    return dict_char

def char_in_proc(dict_):
    new_dict = {}

    from decimal import Decimal
    sum_values = Decimal(str(sum(dict_.values())))

    for value in dict_:
        new_dict[value] = dict_.get(value, 0)
        new_dict[value] = Decimal(str(new_dict[value]))
        new_dict[value] = new_dict[value] * 100 / sum_values
        # new_dict[value] = new_dict[value].quantize(Decimal("1.00"))

    return new_dict
    # return sum(new_dict.values()) # без округления сумма 100.0000000000000000000000000
    # с округлением сумма 100.03
main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
print(char_in_proc(get_count_char(main_str)))
