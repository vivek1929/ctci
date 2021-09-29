# Perform basic string compression by using the counts of repeated character. 
# String aaabbbbccd is a3b4c2d1. If compressed string is not smaller, return original.
# String contains only a-z

def compress_string(init_string):
    compressed_string = ''
    current_char = init_string[0]
    count = 0
    compressed = False
    for each in init_string:
        if each == current_char:
            count += 1
        else:
            if count > 1:
                compressed = True
            compressed_string = compressed_string + current_char + str(count)
            current_char = each
            count = 1
    compressed_string = compressed_string + current_char + str(count)
    if compressed:
        return compressed_string
    return init_string

if __name__ == '__main__':
    test_cases = ['aaabbcdeeefffff', 'abcdefghijkl']
    for each_tc in test_cases:
        out = compress_string(each_tc)
        print(str(out))