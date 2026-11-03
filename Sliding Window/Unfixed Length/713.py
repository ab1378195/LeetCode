class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        ans = left = 0
        prod = 1
        for right, num in enumerate(nums):
            prod *= num
            while prod >= k and left < right:
                prod //= nums[left]
                left += 1
            if prod < k:
                ans += right - left + 1
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.numSubarrayProductLessThanK([10, 5, 2, 6], 100))
    print(solution.numSubarrayProductLessThanK([1, 2, 3], 0))
    print(solution.numSubarrayProductLessThanK([7, 2, 7, 8, 6], 1))
