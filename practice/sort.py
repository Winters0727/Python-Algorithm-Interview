import time
import random
from collections import deque

# test = [num for num in range(1, 11)]
test = [num for num in range(1, 10001)]
random.shuffle(test)

def bubble_sort(arr):
    arr = arr[:]
    length = len(arr)
    for i in range(length):
        for j in range(i, length):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

def insertion_sort(arr):
    arr = arr[:]
    result, index = [], -1
    while arr:
        num = arr.pop()
        if not result:
            result.append(num)
            continue
        for idx, r_num in enumerate(result):
            if num < r_num:
                index = idx
                break
        else:
            result.append(num)
        result.insert(index, num)
    return result

def merge_sort(arr):
    arr = arr[:]
    length = len(arr)
    if length == 1:
        return arr
    else:
        pivot = length//2
        left = deque(merge_sort(arr[:pivot]))
        right = deque(merge_sort(arr[pivot:]))
        result = []
        while left and right:
            if left[0] > right[0]:
                result.append(right.popleft())
            else:
                result.append(left.popleft())
        if left:
            result.extend(left)
        if right:
            result.extend(right)
        return result

def quick_sort(arr):
    arr = arr[:]
    length = len(arr)
    if length < 2:
        return arr
    else:
        pivot_index = length//2
        pivot = arr[pivot_index]
        left, right = [], []
        for num in arr:
            if pivot == num:
                continue
            elif num < pivot:
                left.append(num)
            else:
                right.append(num)
        left = quick_sort(left)
        right = quick_sort(right)
        return left + [pivot] + right

print(f'테스트 시작 : 배열 길이{len(test)}')

start = time.time()
print('bubble sort start')
bubble_sort(test)
end = time.time()
print(f'bubble sort end : {end-start}')

start = time.time()
print('insertion sort start')
insertion_sort(test)
end = time.time()
print(f'insertion sort end : {end-start}')

start = time.time()
print('merge sort start')
merge_sort(test)
end = time.time()
print(f'merge sort end : {end-start}')

start = time.time()
print('quick sort start')
quick_sort(test)
end = time.time()
print(f'quick sort end : {end-start}')

radix_test = test[:]
start = time.time()
print('radix sort start')
radix_test.sort()
end = time.time()
print(f'radix sort end : {end-start}')

print('테스트 종료')