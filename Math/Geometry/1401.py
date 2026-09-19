from math import pow


class Solution:
    def checkOverlap(
        self,
        radius: int,
        xCenter: int,
        yCenter: int,
        x1: int,
        y1: int,
        x2: int,
        y2: int,
    ) -> bool:
        x = max(x1, min(xCenter, x2))
        y = max(y1, min(yCenter, y2))
        return pow(x - xCenter, 2) + pow(y - yCenter, 2) <= pow(radius, 2)


if __name__ == "__main__":
    solution = Solution()
    print(solution.checkOverlap(1, 0, 0, 1, -1, 3, 1))
    print(solution.checkOverlap(1, 1, 1, 1, -3, 2, -1))
    print(solution.checkOverlap(1, 0, 0, -1, 0, 0, 1))
