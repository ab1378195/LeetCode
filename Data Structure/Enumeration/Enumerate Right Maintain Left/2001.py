from typing import List
from collections import defaultdict


class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        cnt = defaultdict(int)
        ans = 0
        for rectangle in rectangles:
            ratio = rectangle[0] / rectangle[1]
            if ratio in cnt:
                ans += cnt[ratio]
            cnt[ratio] += 1
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.interchangeableRectangles([[4, 8], [3, 6], [10, 20], [15, 30]]))
    print(solution.interchangeableRectangles([[4, 5], [7, 8]]))
