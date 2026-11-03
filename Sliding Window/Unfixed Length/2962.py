from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        target = max(nums)
        cnt = 0
        left = ans = 0
        for right, num in enumerate(nums):
            cnt += num == target
            while cnt == k:
                cnt -= nums[left] == target
                left += 1
            ans += left
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.countSubarrays([1, 3, 2, 3, 3], 2))
    print(solution.countSubarrays([1, 4, 2, 1], 3))
