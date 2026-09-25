class Solution:
    """本题用递归处理各种字符串运算的情况,可以写成函数递归,此处使用栈来模拟递归
    """
    def braceExpansionII(self, expression: str) -> list[str]:
        stack = []
        res = set()
        cur = {""}  # 当前处理的字符串集合,添加一个空串避免特判cur为空的情况
        for ch in expression:
            if ch.isalpha():  # 字母
                cur = {s + ch for s in cur}
            elif ch == ",":  # 取并集
                res |= cur
                cur = {""}
            elif ch == "{":  # 递
                stack.append((res, cur))
                res = set()
                cur = {""}
            else:  # "}": 归
                sub_res = res | cur
                res, cur = stack.pop()
                cur = {s + t for s in cur for t in sub_res}
        return sorted(res | cur)


if __name__ == "__main__":
    solution = Solution()
    print(solution.braceExpansionII("{a,b}{c,{d,e}}"))
    print(solution.braceExpansionII("{{a,z},a{b,c},{ab,z}}"))
