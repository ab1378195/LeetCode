from typing import List
from math import inf


class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        left = s = 0
        ans = min_len = inf
        n = len(arr)
        # pre_min[i]为右端点小于i的符合要求的最短子数组长度
        pre_min = [inf] * (n + 1)
        for right, num in enumerate(arr):
            s += num
            while s > target:
                s -= arr[left]
                left += 1
            if s == target:
                ans = min(ans, right - left + 1 + pre_min[left])
                min_len = min(min_len, right - left + 1)
            pre_min[right + 1] = min_len
        if ans == inf:
            return -1
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.minSumOfLengths([3, 2, 2, 4, 3], 3))
    print(solution.minSumOfLengths([7, 3, 4, 7], 7))
    print(solution.minSumOfLengths([4, 3, 2, 6, 2, 3, 4], 6))
