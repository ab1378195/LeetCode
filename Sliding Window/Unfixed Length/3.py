class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        ans = 0
        cur = set()
        for i, c in enumerate(s):
            while c in cur:
                cur.remove(s[left])
                left += 1
            cur.add(c)
            ans = max(ans, i - left + 1)
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.lengthOfLongestSubstring("abcabcbb"))
    print(solution.lengthOfLongestSubstring("bbbbb"))
    print(solution.lengthOfLongestSubstring("pwwkew"))
