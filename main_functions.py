"""
Файл с основными функциями для выполнения задач.
"""
import timeit
import time
from additional_functions import *

def input_two_mas(array1, array2):
    """
    Функция для ввода двух массивов, представляющих большие числа.

    :param array1: Исходный массив, представляющий первое большое число.
    :type array1: list
    :param array2: Исходный массив, представляющий второе большое число.
    :type array2: list
    :return: Два массива, представляющие большие числа, введенные пользователем или сгенерированные случайным образом.
    :rtype: tuple
    """
    print("Выберите опцию 1-2:\n"
          "1. Ввести массивы самостоятельно\n"
          "2. Сгенерировать массивы случайным образом\n")
    option = input()
    if is_int(option):
        option = int(option)
    if option == 1:
        # Ввод двух больших чисел вручную
        array1 = input_large_number()
        array2 = input_large_number()
    elif option == 2:
        # Генерация двух больших чисел случайным образом
        length1 = int(input("Введите количество цифр в случайном массиве: "))
        array1 = generate_random_number(length1)
        length2 = int(input("Введите количество цифр в случайном массиве: "))
        array2 = generate_random_number(length2)
    else:
        print('error')
    print("Первый массив цифр:", array1)
    print("Второй массив цифр:", array2)
    return array1, array2  # Возвращаем массивы

def sum_or_difference_arrays(array1, array2):
    """
    Функция для вычисления суммы или разности двух массивов.

    :param array1: Первый массив.
    :type array1: list
    :param array2: Второй массив.
    :type array2: list
    :return: Сумма или разность элементов двух массивов.
    :rtype: int
    """
    print("Выберите находить сумму или разность массивов:\n"
          "1. Сумму\n"
          "2. Разность")
    sum_or_difference = input()
    if is_int(sum_or_difference):
        sum_or_difference = int(sum_or_difference)
    if sum_or_difference == 1:
        sum1 = sum(number for number in array1)
        sum2 = sum(number for number in array2)
        return sum1 + sum2
    if sum_or_difference == 2:
        sum1 = sum(number for number in array1)
        sum2 = sum(number for number in array2)
        return sum1 - sum2

def input_two_numbers_mas(array1, array2):
    """
    Функция для ввода двух массивов чисел.

    :param array1: Исходный массив чисел.
    :type array1: list
    :param array2: Исходный массив чисел.
    :type array2: list
    :return: Два массива чисел, введенные пользователем или сгенерированные случайным образом.
    :rtype: tuple
    """
    print("Выберите опцию 1-2:\n"
          "1. Ввести массивы самостоятельно\n"
          "2. Сгенерировать массивы случайным образом\n")
    option = input()
    if is_int(option):
        option = int(option)
    if option == 1:
        # Самостоятельный ввод двух числовых массивов
        array1 = input_number_array()
        array2 = input_number_array()
    elif option == 2:
        # Генерация двух числовых массивов случайным образом
        length1 = int(input("Введите количество цифр в случайном массиве: "))
        array1 = generate_random_array(length1)
        length2 = int(input("Введите количество цифр в случайном массиве: "))
        array2 = generate_random_array(length2)
    else:
        print('error')
    print("Первый массив:", array1)
    print("Второй массив:", array2)
    return array1, array2  # Возвращаем массивы

def count_total_numbers_old(array1, array2):
    """
    Функция для подсчета количества общих чисел в двух массивах, включая перевернутые версии.

    :param array1: Первый массив чисел.
    :type array1: list
    :param array2: Второй массив чисел.
    :type array2: list
    :return: Количество общих чисел в двух массивах.
    :rtype: int
    """
    result = 0
    for i in array1:
        for j in array2:
            if i == j or str(i)[::-1] == str(j):
                result += 1
    return result

def count_total_numbers_new(array1, array2):
    """
    Функция для подсчета количества общих чисел в двух массивах, включая перевернутые версии.

    :param array1: Первый массив чисел.
    :type array1: list
    :param array2: Второй массив чисел.
    :type array2: list
    :return: Количество общих чисел в двух массивах.
    :rtype: int
    """
    set1 = set(array1)
    set2 = set(array2)
    reversed_set2 = {str(num)[::-1] for num in set2}

    common_count = len(set1 & set2) + len(set1 & reversed_set2)
    return common_count

def get_matrix():
    """
    Функция для ввода матрицы или генерации случайной матрицы.

    :return: Матрица, введенная пользователем или сгенерированная случайным образом.
    :rtype: list
    """
    print("Выберите опцию 1-2:\n"
          "1. Ввести матрицу самостоятельно\n"
          "2. Сгенерировать матрицу случайным образом\n")
    option = input()
    if is_int(option):
        option = int(option)
    if option == 1:
        # Ввод матрицы вручную
        matrix = input_matrix()
        print("Начальная матрица:\n")
        return matrix
    elif option == 2:
        matrix = generate_random_matrix()
        print("Начальная матрица:\n")
        for row in matrix:
            print(row)
        return matrix
    else:
        print("error")

def rotation_matrix_old(matrix):
    """
    Функция для поворота матрицы на 90 градусов против часовой стрелки.

    :param matrix: Исходная матрица.
    :type matrix: list
    :return: Повернутая матрица.
    :rtype: list
    """
    transposed_matrix = transpose_list_comprehension(matrix)
    rotated_matrix = []
    for row in transposed_matrix[::-1]:
        rotated_matrix.append(row)
    return rotated_matrix

def rotation_matrix_new(matrix):
    """
    Функция для поворота матрицы на 90 градусов против часовой стрелки.

    :param matrix: Исходная матрица.
    :type matrix: list
    :return: Повернутая матрица.
    :rtype: list
    """
    transposed_matrix = transpose_list_comprehension(matrix)
    return [row[::-1] for row in transposed_matrix]

if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    array1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    array2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # Используем timeit для измерения времени выполнения функции 10 раз
    execution_time = timeit.timeit(lambda: count_total_numbers_new(array1, array2), number=10000)

    # Вывод времени выполнения
    average_execution_time = execution_time / 10000
    print(f"Среднее время выполнения функции за 10 выполнений: {average_execution_time:.6f} секунд")
    print(count_total_numbers_new(array1, array2))