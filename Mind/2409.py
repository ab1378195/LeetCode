class Solution:
    def countDaysTogether(
        self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str
    ) -> int:
        days = [0, 0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]

        def transform(date: str) -> int:
            return days[int(date[:2])] + int(date[3:])

        startAlice = transform(arriveAlice)
        endAlice = transform(leaveAlice)
        startBob = transform(arriveBob)
        endBob = transform(leaveBob)
        ans = min(endAlice, endBob) - max(startAlice, startBob) + 1
        if ans < 0:
            return 0
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.countDaysTogether("08-15", "08-18", "08-16", "08-19"))
    print(solution.countDaysTogether("10-01", "10-31", "11-01", "12-31"))
