from typing import List


class Solution:
    """注意子数组和子序列的区别,子数组不需要连续,因此排序后处理更为简单"""

    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = left = 0
        for right, num in enumerate(nums):
            while num - nums[left] > 2 * k:
                left += 1
            ans = max(ans, right - left + 1)
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.maximumBeauty([4, 6, 1, 2], 2))
    print(solution.maximumBeauty([1, 1, 1, 1], 10))
