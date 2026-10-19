class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        less = equal = 0
        for num in nums:
            if num < target:
                less += 1
            elif num == target:
                equal += 1
        return list(range(less, less + equal))


if __name__ == "__main__":
    solution = Solution()
    print(solution.targetIndices([1, 2, 5, 2, 3], 2))
    print(solution.targetIndices([1, 2, 5, 2, 3], 3))
    print(solution.targetIndices([1, 2, 5, 2, 3], 5))
    print(solution.targetIndices([1, 2, 5, 2, 3], 4))
