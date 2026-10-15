from typing import List


class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            s = set()
            for j in range(i, n):
                s.add(nums[j])
                ans += len(s) * len(s)
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.sumCounts([1, 2, 1]))
    print(solution.sumCounts([2, 2]))
