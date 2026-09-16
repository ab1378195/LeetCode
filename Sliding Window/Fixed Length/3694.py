class Solution:
    def distinctPoints(self, s: str, k: int) -> int:
        # 二维坐标变换转化为一维坐标变化
        n = len(s)
        DIRECTIONS = {"L": -(n + 1), "R": n + 1, "D": -1, "U": 1}
        st = {0}
        x = 0
        for i in range(k, n):
            x += DIRECTIONS[s[i]] - DIRECTIONS[s[i - k]]
            st.add(x)
        return len(st)


if __name__ == "__main__":
    solution = Solution()
    print(solution.distinctPoints("LUL", 1))
    print(solution.distinctPoints("UDLR", 4))
    print(solution.distinctPoints("UU", 1))
