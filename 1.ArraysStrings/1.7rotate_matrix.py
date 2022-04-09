# Given an image represent by NxN matrix. Write a method to rotate the image 
# by 90 degrees. 

# Swap in place by considering one layer at a time
# and move from outer layer to each inner layer
def rotate_clockwise(matrix):
    n = len(matrix)
    for layer in range(int(n/2)):
        first = layer
        last = n - 1 - layer
        for i in range(first, last):
            offset = i - first
            top = matrix[first][i]

            matrix[first][i] = matrix[last-offset][first]

            matrix[last-offset][first] = matrix[last][last-offset]

            matrix[last][last-offset] = matrix[i][last]

            matrix[i][last] = top
    
    return matrix

if __name__ == '__main__':
    first_tc_matrix = [['a','b'], ['c','d']]
    second_tc_matrix = [['a','b','c'], ['d','e','f'], ['g','h', 'i']]
    test_cases = [first_tc_matrix, second_tc_matrix]
    for each_tc in test_cases:
        out = rotate_clockwise(each_tc)
        print (out)