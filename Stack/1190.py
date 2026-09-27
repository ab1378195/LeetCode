class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        temp = ""
        for c in s:
            if c == "(":
                stack.insert(0, temp)
                temp = ""
            elif c == ")":
                temp = stack.pop(0) + temp[::-1]
            else:
                temp += c
        return temp


if __name__ == "__main__":
    solution = Solution()
    print(solution.reverseParentheses("(abcd)"))
    print(solution.reverseParentheses("(u(love)i)"))
    print(solution.reverseParentheses("(ed(et(oc))el)"))
