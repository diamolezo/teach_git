def filter_greater(arr: list, value:int) -> list:
    """
        :param arr: list[]
        :param value: int
        :return: list[]
        """
    array = []
    for i in arr:
        if i > value:
            array.append(i)
    return array


def filter_equal(arr: list, value:int) -> list:
    """
        :param arr: list[]
        :param value: int
        :return: list[]
        """
    array = []
    for i in arr:
        if i == value:
            array.append(i)
    return array


def filter_less(arr: list, value:int) -> list:
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


def filter_not_equal(arr: list, value:int) -> list:
    """

    :param arr: list[]
    :param value: int
    :return: list[] array elements < value
    """
    array_elem_not_equal_value = []

    for i in range(len(arr)):
        if arr[i] != value:
            array_elem_not_equal_value.append(arr[i])

    return array_elem_not_equal_value