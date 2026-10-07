class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        # 统计字符串内至多能有target个左括号
        target = left = 0
        for ch in s:
            if ch == "(":
                target += 1
                left += 1
            elif ch == ")" and left > 0:
                left -= 1
        target -= left

        n = len(s)
        ans = []
        path = []

        # 已枚举到s[i],已选left个左括号和right个右括号
        def dfs(i: int, left: int, right: int) -> None:
            # 剪枝
            if left < right or left > target or left + right + n - i < target * 2:
                return
            # 经过剪枝后当走到n时必定为target个左右括号
            if i == n:
                ans.append("".join(path))
                return

            ch = s[i]
            # 不选
            if ch == "(" or ch == ")":
                # 后续所有等于ch的字符都不选,防止[选ch不选ch']和[不选ch选ch']的重复情况被添加
                j = i + 1
                while j < n and s[j] == ch:
                    j += 1
                dfs(j, left, right)

            # 选
            if ch == "(":
                left += 1
            elif ch == ")":
                right += 1
            path.append(ch)
            dfs(i + 1, left, right)
            path.pop()

        dfs(0, 0, 0)
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.removeInvalidParentheses("()())()"))
    print(solution.removeInvalidParentheses("(a)())()"))
    print(solution.removeInvalidParentheses(")("))
