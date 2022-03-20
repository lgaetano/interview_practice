"""
Given a string s, return true if s __can be__ palindrome after 
deleting at most one character from it.

palindrome: same forwards and backwards

Input: s = "catach" -> "catac" 
Output: True

Input: s = "cathac" -> "catac" 
Output: True

2, 2, 2, 2, 1, 3
"tebbem"
"""

from collections import Counter

def is_subset_palindrome(s, i, j):
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1

    return True

def is_palindrome(s):
    l = 0
    r = len(s) - 1 

    while l < r:
        if s[l] != s[r]:
            return is_subset_palindrome(s, l, r - 1) or is_subset_palindrome(s, l - 1, r)

        l += 1
        r -= 1
    
    return False








def validPalindrome(self, s: str) -> bool:
        def check_palindrome(s, i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            
            return True

        i = 0
        j = len(s) - 1
        while i < j:
            # Found a mismatched pair - try both deletions
            if s[i] != s[j]:
                return check_palindrome(s, i, j - 1) or check_palindrome(s, i + 1, j)
            i += 1
            j -= 1
        
        return True


assert is_palindrome("deeee") == False
assert is_palindrome("tebbem") == False
assert is_palindrome("catch") == False
assert is_palindrome("catcah") == False
assert is_palindrome("hcatch") == True