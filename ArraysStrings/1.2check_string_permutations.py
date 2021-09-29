# Given two strings, write a method to decide if one is permutation of other
# dog is a permutation of god

def check_if_string_permutation(string_a, string_b):
    if len(string_a) != len(string_b):
        return False 
    list_a = list(string_a)
    list_b = list(string_b)
    list_a.sort()
    list_b.sort()
    return (list_a == list_b)

if __name__ == '__main__':
    string_one = 'abcdefgh'
    string_two = 'bdfhaceg'

    out = check_if_string_permutation(string_one, string_two)
    print(str(out))