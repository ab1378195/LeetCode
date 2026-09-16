from typing import List


class Solution:
    def maxFreeTime(
        self, eventTime: int, k: int, startTime: List[int], endTime: List[int]
    ) -> int:
        def getFreeTime(i: int) -> int:
            if i == 0:
                return startTime[0]
            if i == n:
                return eventTime - endTime[n - 1]
            return startTime[i] - endTime[i - 1]

        n = len(startTime)
        ans = s = 0
        for i in range(n + 1):
            s += getFreeTime(i)
            if i < k:
                continue
            ans = max(ans, s)
            s -= getFreeTime(i - k)
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxFreeTime(5, 1, [1, 3], [2, 5]))
    print(solution.maxFreeTime(10, 1, [0, 2, 9], [1, 4, 10]))
    print(solution.maxFreeTime(5, 2, [0, 1, 2, 3, 4], [1, 2, 3, 4, 5]))
