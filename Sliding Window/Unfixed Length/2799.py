from typing import List
from collections import Counter, defaultdict


class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        target = len(Counter(nums))
        cnt = defaultdict(int)
        left = ans = 0
        for right, num in enumerate(nums):
            cnt[num] += 1
            while len(cnt) == target:
                if cnt[nums[left]] == 1:
                    del cnt[nums[left]]
                else:
                    cnt[nums[left]] -= 1
                left += 1
            ans += left
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.countCompleteSubarrays([1, 3, 1, 2, 2]))
    print(solution.countCompleteSubarrays([5, 5, 5, 5]))
