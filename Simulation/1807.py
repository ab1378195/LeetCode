from collections import defaultdict


class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        # 查找不到时返回"?"
        substitute = defaultdict(lambda: "?", knowledge)
        ans = ""
        temp = ""
        for c in s:
            if c == "(":
                ans += temp
                temp = ""
            elif c == ")":
                ans += substitute[temp]
                temp = ""
            else:
                temp += c
        return ans + temp


if __name__ == "__main__":
    solution = Solution()
    print(solution.evaluate("(name)is(age)yearsold", [["name", "bob"], ["age", "two"]]))
    print(solution.evaluate("hi(name)", [["a", "b"]]))
    print(solution.evaluate("(a)(a)(a)aaa", [["a", "yes"]]))
