from itertools import pairwise


class Solution:
    """这题有两个关键点:
    1.贪心:题目问的是最少的子数组排序次数,因此选择进行排序的子数组越长所需的排序次数越短;
    2.分类讨论:在意识到要选择最长子数组后就能意识到关键在于s[1:-1]这一段最长的子数组,然后分类讨论最大值和最小值的位置就可以解答本题
    """

    def minOperations(self, s: str) -> int:
        if all(x <= y for x, y in pairwise(s)):
            return 0
        if len(s) == 2:
            return -1
        mn = min(s)
        mx = max(s)
        if s[0] == mn or s[-1] == mx:
            return 1
        if any(ch == mn or ch == mx for ch in s[1:-1]):
            return 2
        return 3


if __name__ == "__main__":
    solution = Solution()
    print(solution.minOperations("dog"))
    print(solution.minOperations("card"))
    print(solution.minOperations("gf"))
