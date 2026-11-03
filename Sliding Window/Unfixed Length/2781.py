from typing import List


class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        fb = set(forbidden)
        ans = left = 0
        for right in range(len(word)):
            for i in range(right, max(right - 10, left - 1), -1):
                if word[i : right + 1] in fb:
                    left = i + 1
                    break
            ans = max(ans, right - left + 1)
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.longestValidSubstring("cbaaaabc", ["aaa", "cb"]))
    print(solution.longestValidSubstring("leetcode", ["de", "le", "e"]))
