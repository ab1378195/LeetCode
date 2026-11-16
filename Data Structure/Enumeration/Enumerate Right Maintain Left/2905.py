from typing import List


class Solution:
    def findIndices(
        self, nums: List[int], indexDifference: int, valueDifference: int
    ) -> List[int]:
        max_idx = 0
        min_idx = 0
        for j in range(indexDifference, len(nums)):
            i = j - indexDifference
            if nums[i] > nums[max_idx]:
                max_idx = i
            if nums[i] < nums[min_idx]:
                min_idx = i
            if nums[max_idx] - nums[j] >= valueDifference:
                return [max_idx, j]
            if nums[j] - nums[min_idx] >= valueDifference:
                return [min_idx, j]
        return [-1, -1]


if __name__ == "__main__":
    solution = Solution()
    print(solution.findIndices([5, 1, 4, 1], 2, 4))
    print(solution.findIndices([2, 1], 0, 0))
    print(solution.findIndices([1, 2, 3], 2, 4))
