class Solution:
    def minFlips(self, s: str) -> int:
        # 关键在于如何判断当前字符串是否为0,1交替,通过index和数值之间的关系实现判断
        # 即判断s[i] mod 2 == i mod 2,等价于异或运算最低位
        ans = n = len(s)
        cnt = 0
        for i in range(2 * n - 1):
            cnt += (ord(s[i % n]) ^ i) & 1
            left = i - n + 1
            if left < 0:
                continue
            ans = min(ans, cnt, n - cnt)
            cnt -= (ord(s[left]) ^ left) & 1
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.minFlips("111000"))
    print(solution.minFlips("010"))
    print(solution.minFlips("1110"))
