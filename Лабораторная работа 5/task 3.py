from random import randint


def get_unique_list_numbers(start, stop, count) -> list[int]:
    if stop - start <= count:
    raise ValueError
    
    unique_list = []
    while len(unique_list) < count:
        number = randint(start, stop)
        if number not in unique_list:
            unique_list.append(number)

    return unique_list


list_unique_numbers = get_unique_list_numbers(-10, 10, 15)
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
