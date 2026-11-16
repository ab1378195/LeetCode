from typing import List


class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        has = set()
        ans = -1
        for num in nums:
            if -num in has:
                ans = max(ans, abs(num))
            else:
                has.add(num)
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.findMaxK([-1, 2, -3, 3]))
    print(solution.findMaxK([-1, 10, 6, 7, -7, 1]))
    print(solution.findMaxK([-10, 8, 6, 7, -2, -3]))
