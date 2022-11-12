
# TODO написать функцию для получения списка уникальных целых чисел

import random
def get_unique_list_numbers() -> list[int]:
    list_unique_numbers = []
    count = 0
    while count < 15:
        numbers = random.randint(-10, 10)
        if numbers not in list_unique_numbers:
            list_unique_numbers.append(numbers)
            count +=1

    return list_unique_numbers

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
