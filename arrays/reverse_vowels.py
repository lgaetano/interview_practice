'''Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both cases.


Input: s = "hello"
Output: "holle"

Input: s = "leetcode"
Output: "leotcede" '''

def reverse_vowels(s):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

    s_list = list(s)
    l = 0
    r = len(s) - 1

    while l < r:
        if s_list[l] not in vowels:
            l += 1
            continue

        elif s_list[l] in vowels and s_list[r] in vowels and s_list[l] != s_list[r]:
            s_list[l], s_list[r] = s_list[r], s_list[l]
            # temp = s_list[l]
            # s_list[l] = s_list[r]
            # s_list[r] = temp

        elif s_list[r] not in vowels and r > 0:
            while s_list[r] not in vowels:
                r -= 1
            s_list[l], s_list[r] = s_list[r], s_list[l]
            # temp = s_list[l]
            # s_list[l] = s_list[r]
            # s_list[r] = temp
        
        l += 1
        r -= 1

    return "".join(s_list)

# def reverse_vowels(s):
#     vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

#     rev_s = s[::-1]

#     vowels_in_s = []
#     for char in rev_s:
#         if char in vowels:
#             vowels_in_s.append(char)

#     s = list(s)

#     vowel_count = 0
#     for i in range(len(s)):
#         if s[i] in vowels:
#             s[i] = vowels_in_s[vowel_count]
#             vowel_count += 1


#     return "".join(s) # Time: O(n) # Space: O(n)


assert reverse_vowels("Marge, let's \"went.\" I await news telegram.") == "Marge, let's \"went.\" i awaIt news telegram."
assert reverse_vowels("cato") == "cota"
assert reverse_vowels("hello") == "holle"
assert reverse_vowels("hoolle") == "heollo"
assert reverse_vowels("aardverk") == "eardvark"
assert reverse_vowels("") == ""
assert reverse_vowels("bcdf") == "bcdf"
assert reverse_vowels("aeiou") == "uoiea"
