class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans = []
        depth = 0
        for ch in s:
            if ch == "(":
                if depth > 0:
                    ans.append("(")
                depth += 1
            else:
                depth -= 1
                if depth > 0:
                    ans.append(")")
        return "".join(ans)


if __name__ == "__main__":
    solution = Solution()
    print(solution.removeOuterParentheses("(()())(())"))
    print(solution.removeOuterParentheses("(()())(())(()(()))"))
    print(solution.removeOuterParentheses("()()"))
