from typing import List
from collections import defaultdict
from math import inf

class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        cnt = defaultdict(int)
        s = 0
        for num in nums:
            cnt[num] += 1
            s += num
        ans = -inf
        for num in sorted(cnt.keys()):
            if cnt[(s - num) / 2]:
                if num * 3 == s and cnt[num] < 2:
                    continue
                ans = max(ans, num)
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.getLargestOutlier([6, -31, 50, -35, 41, 37, -42, 13]))
    print(solution.getLargestOutlier([2, 3, 5, 10]))
    print(solution.getLargestOutlier([-2, -1, -3, -6, 4]))
    print(solution.getLargestOutlier([1, 1, 1, 1, 1, 5, 5]))
