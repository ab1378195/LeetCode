from typing import List
from itertools import pairwise


class Solution:
    """本题可用分组循环"""

    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        ascend_ans = descend_ans = 1
        ascend_left = descend_left = 0
        for i, (prev, cur) in enumerate(pairwise(nums), 1):
            if cur > prev:
                descend_left = i
                ascend_ans = max(ascend_ans, i - ascend_left + 1)
            elif cur < prev:
                ascend_left = i
                descend_ans = max(descend_ans, i - descend_left + 1)
            else:
                ascend_left = descend_left = i
        return max(ascend_ans, descend_ans)


if __name__ == "__main__":
    solution = Solution()
    print(solution.longestMonotonicSubarray([1, 4, 3, 3, 2]))
    print(solution.longestMonotonicSubarray([3, 3, 3, 3]))
    print(solution.longestMonotonicSubarray([3, 2, 1]))
