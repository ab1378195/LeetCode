from typing import List


class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            s = 0
            while num != 0:
                s += num % 10
                num //= 10
            if s == i:
                return i
        return -1


if __name__ == "__main__":
    solution = Solution()
    print(solution.smallestIndex([1, 3, 2]))
    print(solution.smallestIndex([1, 10, 11]))
    print(solution.smallestIndex([1, 2, 3]))
