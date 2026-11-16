from typing import List
from math import inf


class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(key=lambda point: (point[0], -point[1]))
        ans = 0
        for i, (_, y1) in enumerate(points):
            max_y = -inf
            for _, y2 in points[i + 1 :]:
                if y1 >= y2 > max_y:
                    max_y = y2
                    ans += 1
                if max_y == y1:
                    break
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.numberOfPairs([[1, 1], [2, 2], [3, 3]]))
    print(solution.numberOfPairs([[6, 2], [4, 4], [2, 6]]))
    print(solution.numberOfPairs([[3, 1], [1, 3], [1, 1]]))
