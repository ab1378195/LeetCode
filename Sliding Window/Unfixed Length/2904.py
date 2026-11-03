class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        ans = s + "e"
        left = temp = 0
        for right, ch in enumerate(s):
            temp += ch == "1"
            while temp == k:
                if right - left + 1 == len(ans):
                    ans = min(ans, s[left : right + 1])
                elif right - left + 1 < len(ans):
                    ans = s[left : right + 1]
                temp -= s[left] == "1"
                left += 1
        return ans if len(ans) <= len(s) else ""


if __name__ == "__main__":
    solution = Solution()
    print(solution.shortestBeautifulSubstring("100011001", 3))
    print(solution.shortestBeautifulSubstring("1011", 2))
    print(solution.shortestBeautifulSubstring("000", 1))
