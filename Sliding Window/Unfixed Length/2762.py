from typing import List
from collections import defaultdict


class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        left = ans = 0
        cnt = defaultdict(int)
        for right, num in enumerate(nums):
            cnt[num] += 1
            while len(cnt) > 3 or max(cnt.keys()) - min(cnt.keys()) > 2:
                if cnt[nums[left]] == 1:
                    del cnt[nums[left]]
                else:
                    cnt[nums[left]] -= 1
                left += 1
            ans += right - left + 1
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.continuousSubarrays([5, 4, 2, 4]))
    print(solution.continuousSubarrays([1, 2, 3]))
