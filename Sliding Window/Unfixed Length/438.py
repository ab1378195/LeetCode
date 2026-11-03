from collections import defaultdict


class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        ans = []
        cnt = defaultdict(int)
        target = defaultdict(int)
        for ch in p:
            target[ch] += 1
        less = len(target)
        k = len(p)
        for right, ch in enumerate(s):
            cnt[ch] += 1
            if cnt[ch] == target[ch]:
                less -= 1
            left = right - k + 1
            if left < 0:
                continue
            if less == 0:
                ans.append(left)
            if cnt[s[left]] == target[s[left]]:
                less += 1
            cnt[s[left]] -= 1
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.findAnagrams("cbaebabacd", "abc"))
    print(solution.findAnagrams("abab", "ab"))
