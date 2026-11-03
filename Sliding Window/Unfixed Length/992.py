from typing import List
from collections import defaultdict


class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        ans = 0
        left1 = left2 = 0
        less1 = less2 = 0
        cnt1 = defaultdict(int)
        cnt2 = defaultdict(int)
        for right, num in enumerate(nums):
            cnt1[num] += 1
            if cnt1[num] == 1:
                less1 += 1
            cnt2[num] += 1
            if cnt2[num] == 1:
                less2 += 1
            while less1 >= k:
                cnt1[nums[left1]] -= 1
                if cnt1[nums[left1]] == 0:
                    less1 -= 1
                left1 += 1
            while less2 > k:
                cnt2[nums[left2]] -= 1
                if cnt2[nums[left2]] == 0:
                    less2 -= 1
                left2 += 1
            ans += left1 - left2
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.subarraysWithKDistinct([1, 2, 1, 2, 3], 2))
    print(solution.subarraysWithKDistinct([1, 2, 1, 3, 4], 3))
