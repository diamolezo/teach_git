def filter_greater(arr, value):
    ''' возвращает массив из элементов `arr`,
    которые больше `value`.'''
    pass


def filter_less(arr, value):
    ''' возвращает массив из элементов
     `arr`, которые меньше `value`. '''
    pass

# Пусть Студент 1 реализует filter_greater и filter_equal, а Студент 2 - filter_less и
# filter_not_equal !!!

# ИЗМЕНИ разработку СВОЕЙ ФУНКЦИИ, а после, замени имя моей функции filter_less_11111111 на имя по заданию - filter_less!!!
# УДАЧИ!!!

def filter_less_11111111(arr: list, value:int) -> list:
    """

    :param arr: list[]
    :param value: int
    :return: list[] array elements < value
    """
    array_elem_smal_value = []

    for i in range(len(arr)):
        if arr[i] < value:
            array_elem_smal_value.append(arr[i])

    return array_elem_smal_value