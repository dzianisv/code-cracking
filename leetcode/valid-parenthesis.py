"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.

 
"""

chars = { '}':'{', ')':'(', ']':'['}
open_chars = set(chars.values())
close_chars = set(chars.keys())

class Solution(object):
    def isValid(self, s):
        stack = list()
        for c in s:
            if c in open_chars:
                stack.append(c)
            elif c in close_chars:
                if len(stack) == 0:
                    return False
                if stack.pop() != chars[c]:
                    return False

        return len(stack) == 0