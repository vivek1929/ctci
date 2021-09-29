# Implement algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures. 


def without_additional_ds(input_string):
    # Check if the input string contains only ASCII but not Unicode
    # Maximum unique ascii characters are only 128
    if len(input_string) > 128:
        return False

    for i in range(len(input_string)):
        char_to_find = input_string[i]
        rem_string = input_string[i+1:]
        if char_to_find in rem_string:
            return False
    return True

from collections import defaultdict
def with_additional_ds(input_string):
    # Check if the input string contains only ASCII but not Unicode
    # Maximum unique ascii characters are only 128
    if len(input_string) > 128:
        return False

    unique_char_dict = defaultdict(bool)
    for char in input_string:
        if (unique_char_dict[char]):
            return False
        else:
            unique_char_dict[char] = True
    return True

if __name__ == '__main__':
    input_string = 'abcdefghij'

    out = without_additional_ds(input_string)
    print (str(out))

    out = with_additional_ds(input_string)
    print (str(out))