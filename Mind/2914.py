class Solution:
    def minChanges(self, s: str) -> int:
        ans = 0
        for i in range(0, len(s) - 1, 2):
            if s[i] != s[i + 1]:
                ans += 1
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.minChanges("1001"))
    print(solution.minChanges("10"))
    print(solution.minChanges("0000"))
