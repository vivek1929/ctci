# Given a string, find if a permutation of string is a palindrome or not. 
# A string or phase is palindrome if it is same backwards. 
# Permutation is using same characters in different order. 

def check_if_permutation_of_string_a_palindrome(check_string):
    # A string is palindrome must have same characters repeating in even times.
    # And can have maximum of only one other character. 
    odd_strings = {}
    check_string = check_string.lower()
    for each in check_string:
        if each.isalpha():
            if each in odd_strings:
                del odd_strings[each]
            else:
                odd_strings[each] = 1
    if len(odd_strings) > 1:
        return False
    return True

if __name__ == '__main__':
    input_string = 'Tact Coa'
    out = check_if_permutation_of_string_a_palindrome(input_string)
    print(str(out))