from collections import defaultdict


class Solution:
    def similarPairs(self, words: list[str]) -> int:
        cnt = defaultdict(int)
        ans = 0
        for word in words:
            mask = 0
            for ch in word:
                mask |= 1 << (ord(ch) - ord("a"))
            ans += cnt[mask]
            cnt[mask] += 1
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.similarPairs(["aba", "aabb", "abcd", "bac", "aabc"]))
    print(solution.similarPairs(["aabb", "ab", "ba"]))
    print(solution.similarPairs(["nba", "cba", "dba"]))
