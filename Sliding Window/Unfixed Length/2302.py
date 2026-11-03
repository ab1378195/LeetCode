class Solution:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        left = ans = 0
        s = 0
        for right, num in enumerate(nums):
            s += num
            while s * (right - left + 1) >= k:
                s -= nums[left]
                left += 1
            ans += right - left + 1
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.countSubarrays([2, 1, 4, 3, 5], 10))
    print(solution.countSubarrays([1, 1, 1], 5))
