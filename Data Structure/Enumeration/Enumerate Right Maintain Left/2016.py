from typing import List
from math import inf


class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        min_num = inf
        ans = -1
        for num in nums:
            if num - min_num > 0 and num - min_num > ans:
                ans = num - min_num
            min_num = min(min_num, num)
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.maximumDifference([7, 1, 5, 4]))
    print(solution.maximumDifference([9, 4, 3, 2]))
    print(solution.maximumDifference([1, 5, 2, 10]))
