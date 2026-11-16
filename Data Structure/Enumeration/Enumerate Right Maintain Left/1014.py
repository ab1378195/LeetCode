from typing import List


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        best_sightseeing = 0
        ans = 0
        for i, value in enumerate(values):
            ans = max(ans, value + best_sightseeing - i)
            best_sightseeing = max(best_sightseeing, value + i)
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxScoreSightseeingPair([8, 1, 5, 2, 6]))
    print(solution.maxScoreSightseeingPair([1, 2]))
