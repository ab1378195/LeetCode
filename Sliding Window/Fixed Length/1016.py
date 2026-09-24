class Solution:
    """若n的二进制长度为k+1,那么长度为k+1的二进制数为[2^k,n],长度为k的二进制数为[2^(k-1),2^k-1].
    第一个区间有n-2^k+1个数,考虑可能的重叠,需要字符串长度至少为k+1+(n-2^k+1-1),同理第二个区间要求长度至少为k+(2^(k-1)-1),
    即字符串长度m>=max(n-2^k+k+1, 2^(k-1)+k-1).
    将区间[2^(k-1),2^k-1]的数右移一位,可以得到长度为k-1的所有二进制数,因此只需判断长度为k和k+1的二进制数是否都存在即可.
    另外,由于[2^k,n]右移一位能得到[2^(k-1),n//2],所以长度为k的二进制数只用检查[n//2+1, 2^k-1]即可.
    """

    def queryString(self, s: str, n: int) -> bool:
        # 当n=1时,k=0,区间[2^(k-1),2^k-1]不存在,因此进行特判
        if n == 1:
            return "1" in s
        m = len(s)
        k = n.bit_length() - 1
        # 由于本题m和n数值差距较大,因此可以判断长度来进行优化
        if m < max(n - (1 << k) + k + 1, (1 << (k - 1)) + k - 1):
            return False

        def check(k: int, lower: int, upper: int) -> bool:
            """判断s是否拥有[lower,upper]内长度为k的所有二进制数"""
            if lower > upper:
                return True
            seen = set()
            mask = (1 << (k - 1)) - 1
            x = int(s[: k - 1], 2)
            for c in s[k - 1 :]:
                x = ((x & mask) << 1) | int(c)
                if lower <= x <= upper:
                    seen.add(x)
            return len(seen) == upper - lower + 1

        return check(k, n // 2 + 1, (1 << k) - 1) and check(k + 1, 1 << k, n)


if __name__ == "__main__":
    solution = Solution()
    print(solution.queryString("0110", 3))
    print(solution.queryString("0110", 4))
