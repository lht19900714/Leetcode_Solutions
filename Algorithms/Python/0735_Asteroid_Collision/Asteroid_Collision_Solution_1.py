
# Space: O(n)
# Time: O(n)

class Solution:
    def asteroidCollision(self, asteroids):
        # positive asteroid flying to right  "->"
        # negative asteroid flying to left  "<-"

        stack = []

        for asteroid in asteroids:

            while stack:
                if asteroid < 0 < stack[-1]:  # the collision will be happened in this condition only
                    if abs(stack[-1]) > abs(asteroid):
                        break
                    elif abs(stack[-1]) < abs(asteroid):
                        stack.pop()
                        continue
                    elif abs(asteroid) == abs(stack[-1]):
                        stack.pop()
                        break
                else:  # append asteroid in stack for all the other conditions
                    stack.append(asteroid)
                    break
            else:
                stack.append(asteroid)

        return stack



