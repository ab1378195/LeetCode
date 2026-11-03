from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cnt = defaultdict(int)
        left = ans = 0
        for right, ch in enumerate(s):
            cnt[ch] += 1
            while max(cnt.values()) + k < right - left + 1:
                cnt[s[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.characterReplacement("ABAB", 2))
    print(solution.characterReplacement("AABABBA", 1))
