from collections import defaultdict


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        map_list = defaultdict(lambda: -1)
        for i, num in enumerate(nums):
            if map_list[target - num] >= 0:
                return [map_list[target - num], i]
            map_list[num] = i


if __name__ == "__main__":
    solution = Solution()
    print(solution.twoSum([2, 7, 11, 15], 9))
    print(solution.twoSum([3, 2, 4], 6))
    print(solution.twoSum([3, 3], 6))
