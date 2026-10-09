class Solution:
    def minInsertions(self, s: str) -> int:
        cnt = 0
        n = len(s)
        i = 0
        ans = 0
        while i < n:
            if s[i] == "(":
                cnt += 1
                i += 1
                continue

            if cnt > 0:
                cnt -= 1
            else:
                ans += 1

            if i + 1 < n and s[i + 1] == ")":
                i += 2
            else:
                ans += 1
                i += 1
        return ans + cnt * 2


if __name__ == "__main__":
    solution = Solution()
    print(solution.minInsertions("(()))"))
    print(solution.minInsertions("())"))
    print(solution.minInsertions("))())("))
    print(solution.minInsertions("(((((("))
    print(solution.minInsertions(")))))))"))
