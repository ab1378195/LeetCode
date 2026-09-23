from math import inf


class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        total = sum(nums)
        if total < x:
            return -1
        elif total == x:
            return len(nums)
        target = total - x
        s = 0
        left = 0
        ans = -1
        for right, num in enumerate(nums):
            s += num
            while s > target:
                s -= nums[left]
                left += 1
            if s == target:
                ans = max(ans, right - left + 1)
        if ans == -1:
            return ans
        return len(nums) - ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.minOperations([1, 1, 4, 2, 3], 5))
    print(solution.minOperations([5, 6, 7, 8, 9], 4))
    print(solution.minOperations([3, 2, 20, 1, 1, 3], 10))
