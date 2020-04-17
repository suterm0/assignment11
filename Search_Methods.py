def bubble_sort(arr):
    def swap(i, j):
        arr[i], arr[j] = arr[j], arr[i]

    n = len(arr)
    swapped = True

    x = -1
    while swapped:
        swapped = False
        x = x + 1
        for i in range(1, n-x):
            if arr[i - 1] > arr[i]:
                swap(i - 1, i)   # If the numbers aren't in order it swaps with the number next to it in the list until they are in order
                swapped = True
    return arr


def selection_sort(arr):
    for i in range(len(arr)):
        minimum = i

        for j in range(i + 1, len(arr)):
            # Selects the smallest value
            if arr[j] < arr[minimum]:  # Moves all the smaller values to the front half of the list then sorts
                minimum = j
                # then places is at the front of the sorted array
        arr[minimum], arr[i] = arr[i], arr[minimum]
    return arr


def insertion_sort(arr):

    for i in range(len(arr)):
        cursor =  arr[i]
        pos = i

        while pos > 0 and arr[pos - 1] > cursor:      # finds where the number belongs in the list based of position and places it in that spot
            # swap the number down the list
            arr[pos] = arr[pos - 1]
            pos = pos - 1

        arr[pos] = cursor

    return arr


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2         # divides the array into two halves
    # Perform merge_sort on both halves
    left, right = merge_sort(arr[:mid]), merge_sort(arr[mid:])
    return merge(left, right, arr.copy())


def merge(left, right, merged):
    # cuts the list into segments and sorts them individually repeatedly
    left_cursor, right_cursor = 0, 0
    while left_cursor < len(left) and right_cursor < len(right):

        # Sort each one and place it into the result
        if left[left_cursor] <= right[right_cursor]:
            merged[left_cursor+right_cursor]=left[left_cursor]
            left_cursor += 1
        else:
            merged[left_cursor + right_cursor] = right[right_cursor]
            right_cursor += 1

    for left_cursor in range(left_cursor, len(left)):
        merged[left_cursor + right_cursor] = left[left_cursor]

    for right_cursor in range(right_cursor, len(right)):
        merged[left_cursor + right_cursor] = right[right_cursor]

    return merged


def partition(arr, begin, end):
    pivot_idx = begin
    for i in range(begin+1, end+1):
        if arr[i] <= arr[begin]:
            pivot_idx += 1
            arr[i], arr[pivot_idx] = arr[pivot_idx], arr[i]
    arr[pivot_idx], arr[begin] = arr[begin], arr[pivot_idx]
    return pivot_idx        # finds the pivot point and returns it


def quick_sort_recursion(arr, begin, end):
    if begin >= end:        # then moves numbers around the pivot point
        return
    pivot_idx = partition(arr, begin, end)
    quick_sort_recursion(arr, begin, pivot_idx-1)
    quick_sort_recursion(arr, pivot_idx+1, end)
    return arr


def quick_sort(arr, begin=0, end=None):
    if end is None:
        end = len(arr) - 1
    return quick_sort_recursion(arr, begin, end)
