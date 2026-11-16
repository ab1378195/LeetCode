from typing import List
from itertools import accumulate


class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        s = list(accumulate(nums, initial=0))
        ans = 0
        # firstLen窗口在左的情况,维护左侧firstLen窗口最大值
        max_left = 0
        # firstLen窗口在右的情况,维护左侧secondLen窗口最大值
        max_right = 0
        for i in range(firstLen + secondLen, len(s)):
            max_left = max(max_left, s[i - secondLen] - s[i - secondLen - firstLen])
            max_right = max(max_right, s[i - firstLen] - s[i - firstLen - secondLen])
            ans = max(
                ans,
                max_left + s[i] - s[i - secondLen],
                max_right + s[i] - s[i - firstLen],
            )
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxSumTwoNoOverlap([0, 6, 5, 2, 2, 5, 1, 9, 4], 1, 2))
    print(solution.maxSumTwoNoOverlap([3, 8, 1, 3, 2, 1, 8, 9, 0], 3, 2))
    print(solution.maxSumTwoNoOverlap([2, 1, 5, 6, 0, 9, 5, 0, 3, 8], 4, 3))
