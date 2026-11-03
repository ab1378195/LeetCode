from collections import defaultdict


class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        cnt = defaultdict(int)
        left = ans = 0
        for right, ch in enumerate(s):
            cnt[ch] += 1
            while cnt[ch] == k:
                cnt[s[left]] -= 1
                left += 1
            ans += left
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.numberOfSubstrings("abacb", 2))
    print(solution.numberOfSubstrings("abcde", 1))
