"""URLify: Write a method to replace all spaces in a string with '%20: You may assume that the string has sufficient space at the end to hold the additional characters, and that you are given the "true" length of the string. (Note: If implementing in Java, please use a character array so that you can perform this operation in place.)

EXAMPLE
Input: "Mr John Smith    ",  13
Output: "Mr%20John%20Smith"

Input: "",  0
Output: ""

Input: "cat in the hat    ",  14
Output: "cat%20in%20the%20hat"


split on spaces
join %20
"""

# def urlify(string, true_length): #Time: O(n) Space: O(n)
#     string = string.rstrip()
#     words = string.split()
#     return "%20".join(words)

# Alternate
def urlify(string, true_length): #Time: O(n) Space: O(n)
    return string[:true_length].replace(" ", "%20")

if __name__ == '__main__':
    assert urlify("Mr John Smith    ",  13) == "Mr%20John%20Smith"
    assert urlify("cat in the hat    ",  14) == "cat%20in%20the%20hat"
    assert urlify("", 0) == ""
