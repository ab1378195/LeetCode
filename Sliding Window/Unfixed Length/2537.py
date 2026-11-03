from typing import List
from collections import defaultdict


class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        left = ans = 0
        cnt = defaultdict(int)
        s = 0
        for right, num in enumerate(nums):
            s += cnt[num]
            cnt[num] += 1
            while s >= k:
                if cnt[nums[left]] == 1:
                    del cnt[nums[left]]
                else:
                    cnt[nums[left]] -= 1
                s -= cnt[nums[left]]
                left += 1
            ans += left
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.countGood([1, 1, 1, 1, 1], 10))
    print(solution.countGood([3, 1, 4, 3, 2, 2, 4], 2))
    print(solution.countGood([2, 1, 3, 1, 2, 2, 3, 3, 2, 2, 1, 1, 1, 3, 1], 11))
