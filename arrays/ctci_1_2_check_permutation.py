""" Given two strings, write a method to determine if one is a permutation of the other

Input: "cat", "tac"
Output: True

Input: "cat", "tap"
Output: False

Input: "aat", "taa"
Output: True

Input: "", ""
Output: False

Input: "catc", "cat"
Output: False

"""
def create_freq_map(string):
    freq_map = {}

    for char in string:
        freq_map[char] = freq_map.get(char, 0) + 1

    return freq_map
        

# def is_permutation(str1, str2): # Time O(n) | Space O(n)
#     # validation
#     if str1 == "" or str2 == "":
#         return False
#     if len(str1) != len(str2):
#         return False

#     str1_freq = create_freq_map(str1)
#     str2_freq = create_freq_map(str2)

#     return str1_freq == str2_freq

# Alternate method using Counter class
from collections import Counter

def is_permutation(str1, str2):
    # validation
    if str1 == "" or str2 == "":
        return False
    
    if len(str1) != len(str2):
        return False

    return Counter(str1) == Counter(str2)


if __name__=='__main__':
    assert is_permutation("cat", "tac") == True
    assert is_permutation("", "") == False
    assert is_permutation("cat", "tap") == False
    assert is_permutation("taa", "ata") == True
    assert is_permutation("the cat", "thecat") == False
