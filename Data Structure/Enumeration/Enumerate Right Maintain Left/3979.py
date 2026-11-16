class Solution:
    def maxValidPairSum(self, nums: list[int], k: int) -> int:
        max_num = nums[0]
        ans = 0
        for i, num in enumerate(nums[k:], k):
            ans = max(ans, num + max_num)
            max_num = max(max_num, nums[i - k + 1])
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxValidPairSum([1, 3, 5, 2, 8], 2))
    print(solution.maxValidPairSum([5, 1, 9], 1))
