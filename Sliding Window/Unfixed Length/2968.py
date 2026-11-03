from typing import List


class Solution:
    """本题关键在于意识到:对于一个数组,想要用最少操作次数提高众数频率,则众数应选择为中位数"""

    def maxFrequencyScore(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = ans = s = 0
        for right, num in enumerate(nums):
            s += num - nums[(left + right) // 2]
            while s > k:
                s += nums[left] - nums[(left + right + 1) // 2]
                left += 1
            ans = max(ans, right - left + 1)
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxFrequencyScore([1, 2, 6, 4], 3))
    print(solution.maxFrequencyScore([1, 4, 4, 2, 4], 0))
