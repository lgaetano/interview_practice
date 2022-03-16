"""
Given a string s containing just the characters '(', ')', '{', '}', 
'[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Input: s = "()"
Output: true

Input: s = "()[]{}"
Output: true

Input: s = "(]"
Output: false
"""

def is_valid(s):
    # Odd length is false
    if len(s) % 2 != 0:
        return False

    # dictionary to store brackets 
    d = {
        "{" : "}",
        "[" : "]",
        "(" : ")"
    }

    stack = []

    for char in s:
        # For empty list and closing bracket
        if len(stack) == 0 and char in d.values():
            return False
        # All opening brackets are added to stack
        elif char in d:
            stack.append(char)
        # For closing bracket that matches last item in list
        elif len(stack) > 0 and char in d.values() and char == d[stack[-1]]:
            stack.pop()
        # For closing bracket that does not match last item in list
        else: 
            return False

    return len(stack) == 0


assert is_valid("{}{}[][]()") == True
assert is_valid("{}{}[[]()") == False
assert is_valid("{()()}()") == True
assert is_valid("{(]()}())") == False
assert is_valid("([}}])") == False
assert is_valid("){") == False