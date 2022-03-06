"""
I. Implement an alogrithm to determine if a string has all 
unique characters. 

II. What if you cannot use additional data structures?

Input: "cat"
Output: True

Input: "cac"
Output: False

Input: ""
Output: False
"""
# I. 
# def is_unique(string):
#     if string == "":
#         return False
 
#     hash_map = {}

#     for char in string:
#         if char in hash_map:
#             return False
#         else:
#             hash_map[char] = hash_map.get(char, 0) + 1
#     return True

#II.
def is_unique(string):
    if string == '':
        return False

    for i in range(len(string)):
        if string[i] in string[:i] or string[i] in string[i+1:]:
            return False
    return True


if __name__ == '__main__':
    assert is_unique("cat") == True
    assert is_unique("cac") == False
    assert is_unique("") == False
    assert is_unique("catt")  == False
    assert is_unique("nnat") == False
