# In a MxN matrix, if any element is zero, update entire row and column with 0.

import copy

def set_zero(matrix, m, n):
    # Set entire row and colume to 0's
    for i in range(len(matrix[m])):
        matrix[m][i] = 0
    for j in range(len(matrix)):
        matrix[j][n] = 0
    return matrix

def zero_matrix(init_matrix):
    # Since matrix is a list contains list
    # Shallow copy giving trouble. So deep copy
    # is must
    final_matrix = copy.deepcopy(init_matrix)
    for i in range(len(init_matrix)):
        for j in range(len(init_matrix[i])):
            if init_matrix[i][j] == 0:
                final_matrix = set_zero(final_matrix, i, j)
    return final_matrix


if __name__ == '__main__':
    first_tc_matrix = [[1,2,3],[4,5,0]]
    second_tc_matrix = [[1,1,1,1,1], [1,1,1,1,1], [1,1,0,1,1], [1,1,1,1,0], [1,1,1,1,1]]
    test_cases = [first_tc_matrix, second_tc_matrix]
    for each_tc in test_cases:
        out = zero_matrix(each_tc)
        print (out)