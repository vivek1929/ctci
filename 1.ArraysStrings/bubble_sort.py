# Sorting using bubble technique with bcr of O(n)

def do_bubble_sort(array_to_sort):
    counter = 0
    for i in range(len(array_to_sort)-1):
        swapped = False
        for j in range(len(array_to_sort)-1-i):
            counter += 1
            if array_to_sort[j] > array_to_sort[j +1]:
                swapped = True
                array_to_sort[j] = array_to_sort[j] + array_to_sort[j+1]
                array_to_sort[j+1] = array_to_sort[j] - array_to_sort[j+1]
                array_to_sort[j] = array_to_sort[j] - array_to_sort[j+1]
        if not swapped:
            print('Total iterations are {}'.format(counter))
            return array_to_sort
    print('Total iterations is {}'.format(counter))
    return array_to_sort

# Unsorted array
input_array = [4, 6, 45, 21, 75, 32, 1,53]

# O(n^2) is time complexity
print(*do_bubble_sort(input_array))

# Sorted array
input_array = [1, 2, 3, 4, 5, 6, 7, 8]

# O(n) is time complexity
print(*do_bubble_sort(input_array))