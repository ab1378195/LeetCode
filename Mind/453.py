from typing import List


class Solution:
    def minMoves(self, nums: List[int]) -> int:
        return sum(nums) - min(nums) * len(nums)


if __name__ == "__main__":
    solution = Solution()
    print(solution.minMoves([1, 2, 3]))
    print(solution.minMoves([1, 1, 1]))
