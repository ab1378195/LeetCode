class Solution:
    """要使嵌套深度最少,则考虑A,B均分嵌套深度,如果是最大深度/2均分需要先求出最大深度。
    改为按照深度的奇偶分配,则可以一次遍历完成。
    """

    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        # [0,i]中i个括号有L个左括号,R个右括号,则i=L+R
        # 若seq[i]为左括号,则seq[i]深度为L-R=i-2R,模2得奇偶性为i mod 2
        # 若seq[i]为右括号,则seq[i]深度为L-R-1=i-2R-1,模2得奇偶性为(i-1) mod 2,为不处理负数,可等价为(i+1) mod 2
        # 左括号和右括号ASCII分别为40和41,进一步简化为(i+ (seq[i] mod 2)) mod 2
        return [(i + ord(c)) % 2 for i, c in enumerate(seq)]


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxDepthAfterSplit("(()())"))
    print(solution.maxDepthAfterSplit("()(())()"))
