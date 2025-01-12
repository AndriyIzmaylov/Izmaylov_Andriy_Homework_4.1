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
    non_zero_numbers = [number for number in incoming_list_of_numbers if number != 0]
    zero_count = incoming_list_of_numbers.count(0)
    return non_zero_numbers + [0] * zero_count


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
