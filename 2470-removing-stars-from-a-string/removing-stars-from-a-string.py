class Solution:
    def removeStars(self, s: str) -> str:
        # If the problem involves performing an operation on the previous index based on a certain condition,
        # consider using a stack data structure to help solve the problem.

        stack = []

        for char in s:
            if char == '*' and stack:
                stack.pop() 
            else:
                stack.append(char)

        return ''.join(stack)