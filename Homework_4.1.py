# Написати програму, яка переміщає всі нулі у кінець списку. Ваше завдання — змінити
# список так, щоб усі нулі опинилися наприкінці списку. Порядок ненульових чисел має
# зберегтися!
# Приклад:
# [0, 1, 0, 12, 3] -> [1, 12, 3, 0, 0]
# [0] -> [0]
# [1, 0, 13, 0, 0, 0, 5] -> [1, 13, 5, 0, 0, 0, 0]
# [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0] -> [9, 7, 31, 45, 45, 45, 96, 0, 0, 0, 0, 0, 0, 0]
# Для перевірки коректності роботи Вашого коду використовуйте приклади вище.Робити
# запит на введення даних від користувача не потрібно.

def define_and_move_zeros_to_end(incoming_list_of_numbers):
    index_of_zeros = 0
    for numbers in incoming_list_of_numbers:
        if numbers == 0:
            index_of_zeros += 1
            incoming_list_of_numbers.remove(0)

    incoming_list_of_numbers.extend([0] * index_of_zeros)
    return incoming_list_of_numbers


test_cases = [
    [0],
    [0, 1, 0, 12, 3],
    [1, 0, 13, 0, 0, 0, 5],
    [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
]

for case in test_cases:
    print(f"Entry list: {case}")
    print(f"Result: {define_and_move_zeros_to_end(case)}")
    print("-" * 40)
