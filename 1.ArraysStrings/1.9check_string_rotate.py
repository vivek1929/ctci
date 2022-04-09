# Assume we have a method isSubstring which checks if one string is subset of other. 
# Given two strings, write a code to check if second string is rotation of first
# string using only one call to isSubstring
# E.g: waterbottle is a rotation of erbottlewat

def is_substring(s1, s2):
    return (s2 in s1)

def is_rotation(s1, s2):
    if len(s1) != len(s2):
        return False
    # A rotation splits string to two parts say x,y
    # Rotated string is represented by yx while initial
    # string is xy. Whatsoever yx is always substring of
    # xyxy. So adding s1 + s1
    s1 = s1 + s1
    return is_substring(s1, s2)

if __name__ == '__main__':
    test_cases = [('waterbottle','erbottlewat'),('monsoon', 'soonmno')]
    for each_tc in test_cases:
        out = is_rotation(*each_tc)
        print (out)