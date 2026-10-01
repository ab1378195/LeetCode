class Solution:
    def maxFrequency(self, nums: list[int], k: int) -> int:
        nums.sort()
        left = ans = s = 0
        for right, num in enumerate(nums):
            s += num
            while s + k < (right - left + 1) * num:
                s -= nums[left]
                left += 1
            ans = max(ans, right - left + 1)
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxFrequency([1, 2, 4], 5))
    print(solution.maxFrequency([1, 4, 8, 13], 5))
    print(solution.maxFrequency([3, 9, 6], 2))
