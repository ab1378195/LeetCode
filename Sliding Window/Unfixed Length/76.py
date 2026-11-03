from collections import Counter


class Solution:
    """defaultdict比Counter快"""

    def minWindow(self, s: str, t: str) -> str:
        targets = Counter(t)
        ans = s + "a"
        left = 0
        cnt = Counter()
        less = len(targets)
        for right, ch in enumerate(s):
            cnt[ch] += 1
            if cnt[ch] == targets[ch]:
                less -= 1
            while less == 0:
                if right - left + 1 < len(ans):
                    ans = s[left : right + 1]
                if cnt[s[left]] == targets[s[left]]:
                    less += 1
                cnt[s[left]] -= 1
                left += 1
        return "" if len(ans) > len(s) else ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.minWindow("ADOBECODEBANC", "ABC"))
    print(solution.minWindow("a", "a"))
    print(solution.minWindow("a", "aa"))
