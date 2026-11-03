from typing import List
from collections import defaultdict
from math import inf


class Solution:
    def minLength(self, nums: List[int], k: int) -> int:
        left = s = 0
        cnt = defaultdict(int)
        ans = inf
        for right, num in enumerate(nums):
            cnt[num] += 1
            if cnt[num] == 1:
                s += num
            while s >= k:
                ans = min(ans, right - left + 1)
                if cnt[nums[left]] == 1:
                    s -= nums[left]
                    del cnt[nums[left]]
                else:
                    cnt[nums[left]] -= 1
                left += 1
        return -1 if ans == inf else ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.minLength([2, 2, 3, 1], 4))
    print(solution.minLength([3, 2, 3, 4], 5))
    print(solution.minLength([5, 5, 4], 5))
    print(solution.minLength([6, 6, 11], 12))
