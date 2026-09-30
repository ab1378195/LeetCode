class Solution:
    """似乎这类简单的判断用int统计不合规次数也会比bool的逻辑更简化,能省去bool变量较复杂的if处理,while条件也更简单
    """
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        left = 0
        ans = 1
        repeat = False
        for right, c in enumerate(s[1:], 1):
            while repeat and c == s[right - 1]:
                if s[left] == s[left + 1]:
                    left += 1
                    break
                left += 1
            if c == s[right - 1]:
                repeat = True
            ans = max(ans, right - left + 1)
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.longestSemiRepetitiveSubstring("52233"))
    print(solution.longestSemiRepetitiveSubstring("5494"))
    print(solution.longestSemiRepetitiveSubstring("1111111"))
