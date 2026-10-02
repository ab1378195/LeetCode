class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        def dfs(left: int, right: int, cur: str, ans: list[str]):
            if right == 0:
                ans.append(cur)
                return
            if left > 0:
                cur += "("
                dfs(left - 1, right, cur, ans)
                cur = cur[:-1]
            if left < right:
                cur += ")"
                dfs(left, right - 1, cur, ans)
                cur = cur[:-1]

        ans = []
        dfs(n, n, "", ans)
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.generateParenthesis(3))
    print(solution.generateParenthesis(1))
