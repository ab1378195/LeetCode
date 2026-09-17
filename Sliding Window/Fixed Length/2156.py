class Solution:
    def subStrHash(
        self, s: str, power: int, modulo: int, k: int, hashValue: int
    ) -> str:
        # 由于本题哈希计算的定义,倒序滑窗更新时更方便
        # ord()&31可得到字母的字典index,大小写字母均适用
        # 注意位运算优先级很低,需要补括号
        n = len(s)
        p = pow(power, k - 1, modulo)
        h = ans = 0
        for i in range(n - 1, -1, -1):
            h = (h * power + (ord(s[i]) & 31)) % modulo
            right = i + k - 1
            if right >= n:
                continue
            if h == hashValue:
                ans = i
            h = (h - (ord(s[right]) & 31) * p) % modulo
        return s[ans : ans + k]


if __name__ == "__main__":
    solution = Solution()
    print(solution.subStrHash("leetcode", 7, 20, 2, 0))
    print(solution.subStrHash("fbxzaad", 31, 100, 3, 32))
