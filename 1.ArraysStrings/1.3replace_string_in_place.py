# Write a method to replace all spaces in string with '%20'.
# You may assume that string has enough spaces at end to 
# perform replace in place.

def replace_in_place(input_string):
    mutable_string = list(input_string)
    for i in range(len(mutable_string)):
        if mutable_string[i] == ' ':
            for j in range(1, len(mutable_string)-(i+2)):
                mutable_string[len(mutable_string)-j] = mutable_string[len(mutable_string)-j-2]
            mutable_string[i] = '%'
            mutable_string[i+1] = '2'
            mutable_string[i+2] = '0'
    return (''.join(mutable_string))

if __name__ == '__main__':
    input_string = 'Mr John Smith    '
    out = replace_in_place(input_string)
    print(out)