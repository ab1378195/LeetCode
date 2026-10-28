class Solution:
    def minOperations(self, nums: list[int]) -> int:
        n = len(nums)
        nums = sorted(set(nums))
        ans = left = 0
        for i, num in enumerate(nums):
            while nums[left] < num - n + 1:
                left += 1
            ans = max(ans, i - left + 1)
        return n - ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.minOperations([4, 2, 5, 3]))
    print(solution.minOperations([1, 2, 3, 5, 6]))
    print(solution.minOperations([1, 10, 100, 1000]))
