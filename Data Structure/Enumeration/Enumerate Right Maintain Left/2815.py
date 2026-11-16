from typing import List


class Solution:
    def maxSum(self, nums: List[int]) -> int:
        has = {}
        ans = -1
        for num in nums:
            key = 0
            temp = num
            while temp > 0:
                key = max(key, temp % 10)
                temp //= 10
            if key in has:
                ans = max(ans, has[key] + num)
                has[key] = max(has[key], num)
            else:
                has[key] = num
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxSum([51, 71, 17, 24, 42]))
    print(solution.maxSum([1, 2, 3, 4]))
