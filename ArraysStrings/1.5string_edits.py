# There are three types of edits on a string: Insert or  Delete or replace a character.
# Given two strings, find if second string is <=1 edits away. 

def one_edit_insert(string_a, string_b):
    for i in range(len(string_a)):
        if string_a[i] != string_b[i]:
            string_b = string_b[:i] + string_a[i] + string_b[i:]
    return (string_a, string_b)

def one_edit_replace(string_a, string_b):
    for i in range(len(string_a)):
        if string_a[i] != string_b[i]:
            if i == 0:
                string_b = string_a[i] + string_b[i+1:]
            else:
                string_b = string_b[:i-1] + string_a[i] + string_b[i:]
    return (string_a, string_b)

def check_string_edits(string_a, string_b):
    if (abs(len(string_a) - len(string_b)) > 1):
        return False
    if len(string_a) > len(string_b):
        string_a, string_b = one_edit_insert(string_a, string_b)
    if len(string_a) == len(string_b):
       string_a, string_b = one_edit_replace(string_a, string_b)
    return (string_a == string_b)
if __name__ == '__main__':
    test_cases = [('pale','ple'), ('pale','bale'), ('ale','le')]
    for each_tc in test_cases:
        out = check_string_edits(*each_tc)
        print(str(out))