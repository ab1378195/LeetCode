class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        ans = 0
        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            elif len(stack) > 1:
                stack.pop()
                ans = max(ans, i - stack[-1])
            else:
                stack[0] = i
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.longestValidParentheses("(()"))
    print(solution.longestValidParentheses(")()())"))
    print(solution.longestValidParentheses("()(()"))
