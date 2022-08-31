# -*- coding: utf-8 -*-
"""
Time:2022/8/26 17:46
Author:CAOZHENG
File:test.py
"""

sum = lambda a, b: a * b

print(sum(2, 6))


def bubble_sort(arr_list):
    """
    冒泡排序
    :param arr_list: 待排序列表
    :return:
    """
    for i in range(len(arr_list)):
        for j in range(len(arr_list) - i - 1):
            if arr_list[j] > arr_list[j + 1]:
                arr_list[j], arr_list[j + 1] = arr_list[j + 1], arr_list[j]
    print(arr_list)
    return arr_list


def partition(arr_list, low, high):
    i = low - 1  # 最小元素索引
    pivot = arr_list[high]

    for j in range(low, high):
        # 当前元素小于或等于 pivot
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr_list, low, high):
    """
    快速排序
    :param arr_list: 待排序列表
    :param low:起始索引
    :param high:结束索引
    :return:
    """
    if low < high:
        pi = partition(arr_list, low, high)
        quick_sort(arr_list, low, pi - 1)
        quick_sort(arr_list, pi + 1, high)
    # print(arr_list)
    return arr_list


if __name__ == "__main__":
    arr = [5, 2, 7, 2, 7, 1, 3, 6, 9, 2, 3, 1]
    # bubble_sort(arr)
    quick_sort(arr, 0, len(arr) - 1)
    print(arr)
