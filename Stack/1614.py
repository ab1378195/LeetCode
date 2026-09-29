class Solution:
    # 实际上由于本题只用统计嵌套深度,不需要依据嵌套进行某些处理,所以可以不用stack,只用一个int统计长度即可
    def maxDepth(self, s: str) -> int:
        stack = []
        ans = 0
        for c in s:
            if c == "(":
                stack.append("(")
            elif c == ")":
                ans = max(ans, len(stack))
                stack.pop()
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxDepth("(1+(2*3)+((8)/4))+1"))
    print(solution.maxDepth("(1)+((2))+(((3)))"))
    print(solution.maxDepth("()(())((()()))"))
