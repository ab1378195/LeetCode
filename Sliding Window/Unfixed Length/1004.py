class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        ans = left = cnt = 0
        for right, num in enumerate(nums):
            cnt += 1 - num
            while cnt > k:
                cnt -= 1 - nums[left]
                left += 1
            ans = max(ans, right - left + 1)
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.longestOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2))
    print(
        solution.longestOnes(
            [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3
        )
    )
