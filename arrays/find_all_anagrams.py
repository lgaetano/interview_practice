"""
Given two strings s and p, 
return an array of all the start indices of p's anagrams in s. 
You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters 
of a different word or phrase, typically using __all__ the original 
letters exactly once.

anagrams:
cat -> tac

s = catac
    ^ ^
p = cat

output: [0, 2]
"""

# TOO SLOW TRY TO IMPLEMENT Counter method?

from collections import Counter

def mutual_anagrams(s, p):
    result = []

    if len(p) > len(s):
        return result

    start = 0
    end = len(p)

    p_hash = Counter(p)


    # 1, 2, 3, 4, 5, 6
    while start < len(s) - len(p) + 1:
        # hash map of s substring
        sub_s_hash = Counter(s[start:start + end])
        
        if p_hash == sub_s_hash:
            result.append(start)
        start += 1

    return result



# def mutual_anagrams(s, p):
#     result = []

#     if len(p) > len(s): 
#          return result
    
#     start = 0
#     end = len(p)

#     p_list = list(p)
#     p_list.sort()

#     while start < len(s) - len(p) + 1:
#         sub_str = list(s[start:end])
#         sub_str.sort()

#         if sub_str == p_list:
#             result.append(start)
            
#         start += 1
#         end += 1

#     return result



assert mutual_anagrams("catxtac", "tca") == [0, 4]
assert mutual_anagrams("cattac", "xse") == []
assert mutual_anagrams("cattac", "xsedsfsagasdf") == []