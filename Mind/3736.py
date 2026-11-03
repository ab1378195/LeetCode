from typing import List


class Solution:
    def minMoves(self, nums: List[int]) -> int:
        return max(nums) * len(nums) - sum(nums)


if __name__ == "__main__":
    solution = Solution()
    print(solution.minMoves([2, 1, 3]))
    print(solution.minMoves([4, 4, 5]))
