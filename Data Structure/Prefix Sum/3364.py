from typing import List
from math import inf
from itertools import accumulate
from sortedcontainers import SortedList


class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        ans = inf
        s = list(accumulate(nums, initial=0))
        sl = SortedList()
        for i in range(l, len(nums) + 1):
            sl.add(s[i - l])
            k = sl.bisect_left(s[i])
            if k:
                ans = min(ans, s[i] - sl[k - 1])
            if i >= r:
                sl.remove(s[i - r])
        return -1 if ans == inf else ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.minimumSumSubarray([3, -2, 1, 4], 2, 3))
    print(solution.minimumSumSubarray([-2, 2, -3, 1], 2, 3))
    print(solution.minimumSumSubarray([1, 2, 3, 4], 2, 4))
    print(solution.minimumSumSubarray([17, 13], 1, 2))
