class Solution:
    def maxDistance(self, arrays: list[list[int]]) -> int:
        min_value = arrays[0][0]
        max_value = arrays[0][-1]
        ans = 0
        for array in arrays[1:]:
            ans = max(ans, array[-1] - min_value, max_value - array[0])
            min_value = min(min_value, array[0])
            max_value = max(max_value, array[-1])
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxDistance([[1, 2, 3], [4, 5], [1, 2, 3]]))
    print(solution.maxDistance([[1], [1]]))
