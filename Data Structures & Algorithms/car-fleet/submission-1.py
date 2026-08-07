import math
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sortedP = sorted(zip(position, speed), reverse = True)
        stack = []
        for p, s in sortedP:
            time = (target - p) / s
            if stack and time <= stack[-1]:
                continue
            else:
                stack.append(time)
        return len(stack)