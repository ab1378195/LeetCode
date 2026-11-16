from typing import List


class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        cnt = [0] * 24
        ans = 0
        for hour in hours:
            ans += cnt[(24 - hour % 24) % 24]
            cnt[hour % 24] += 1
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.countCompleteDayPairs([12, 12, 30, 24, 24]))
    print(solution.countCompleteDayPairs([72, 48, 24, 3]))
