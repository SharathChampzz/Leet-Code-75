class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_brackets = ['(', '{', '[']

        pairings = {
            '(' : ')',
            '[' : ']',
            '{' : '}'
        }

        for char in s:
            if char in open_brackets:
                stack.append(char)
            else:
                if not stack:
                    return False
                    
                open_bracket = stack.pop()

                if pairings[open_bracket] != char:
                    return False

        return False if stack else True

