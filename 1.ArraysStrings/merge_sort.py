
import copy

def merge_sort(input):
    if len(input) < 2:
        return
    mid = len(input)//2

    left = input[:mid]
    right = input[mid:]

    merge_sort(left)
    merge_sort(right)

    i = j = 0
    k = 0

    op_list = copy.deepcopy(input)

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            input[k] = left[i]
            i += 1
        else:
            input[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        input[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        input[k]=right[j]
        j += 1
        k += 1

    return input

if __name__ == '__main__':
    input_list = [5, 3, 19, 1, 94, 2]
    op = merge_sort(input_list)
    print(op)