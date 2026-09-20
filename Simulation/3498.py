class Solution:
    def reverseDegree(self, s: str) -> int:
        ans = 0
        for i, c in enumerate(s):
            ans += (i + 1) * (27 - (ord(c) & 31))
        return ans
        # 用z的下一个字符{来减就能得到字母反转度    
        # enumerate可以设置起始index
        return sum((ord('{') - ord(c)) * i for i, c in enumerate(s, 1))


if __name__ == "__main__":
    solution = Solution()
    print(solution.reverseDegree("abc"))
    print(solution.reverseDegree("zaza"))
