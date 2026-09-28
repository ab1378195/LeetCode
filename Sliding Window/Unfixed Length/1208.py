class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        # 预先初始化好costs速度会更快
        ans = left = 0
        for right, (c1, c2) in enumerate(zip(s, t)):
            maxCost -= abs(ord(c1) - ord(c2))
            while maxCost < 0:
                maxCost += abs(ord(s[left]) - ord(t[left]))
                left += 1
            ans = max(ans, right - left + 1)
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.equalSubstring("abcd", "bcdf", 3))
    print(solution.equalSubstring("abcd", "cdef", 3))
    print(solution.equalSubstring("abcd", "acde", 0))
