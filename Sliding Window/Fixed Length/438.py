from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        cnt = Counter(p)
        less = len(cnt)
        ans = []
        m = len(p)
        for i, c in enumerate(s):
            cnt[c] -= 1
            if cnt[c] == 0:
                less -= 1
            left = i - m + 1
            if left < 0:
                continue
            if less == 0:
                ans.append(left)
            out = s[left]
            if cnt[out] == 0:
                less += 1
            cnt[out] += 1
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.findAnagrams("cbaebabacd", "abc"))
    print(solution.findAnagrams("abab", "ab"))
