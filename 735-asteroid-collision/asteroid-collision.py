class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """
        Asteroids will collide only when a positive element encounters a new negative element.
        If there is already a negative element and a new positive element comes in, they will not collide as they are moving in different directions.

        To simplify, we will focus on when negative elements come in and analyze all the positive elements present at the end.
        """
        stack = []

        for asteroid in asteroids:
            if asteroid > 0:
                stack.append(asteroid)
            else:
                while stack and stack[-1] > 0:
                    if abs(stack[-1]) > abs(asteroid):  # New asteroid is smaller, so it will explode
                        break
                    elif abs(stack[-1]) == abs(asteroid):  # If same size, both explode
                        stack.pop()
                        break
                    else:
                        stack.pop()  # New asteroid is bigger
                else:
                    stack.append(asteroid)

        return stack
