class Solution:
    """在入栈时可以直接存入对应的反括号,而不是存原括号是什么,这样出栈比较的时候更方便"""

    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == "(" or c == "[" or c == "{":
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                out = stack.pop()
                if (
                    c == ")"
                    and out != "("
                    or c == "]"
                    and out != "["
                    or c == "}"
                    and out != "{"
                ):
                    return False
        return len(stack) == 0


if __name__ == "__main__":
    solution = Solution()
    print(solution.isValid("()"))
    print(solution.isValid("()[]{}"))
    print(solution.isValid("(]"))
    print(solution.isValid("([])"))
    print(solution.isValid("([)]"))
