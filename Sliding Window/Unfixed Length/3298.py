from collections import Counter


class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        left = ans = 0
        cnt = Counter(word2)
        less = len(cnt)
        for right, ch in enumerate(word1):
            cnt[ch] -= 1
            if cnt[ch] == 0:
                less -= 1
            while less == 0:
                cnt[word1[left]] += 1
                if cnt[word1[left]] == 1:
                    less += 1
                left += 1
            ans += left
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.validSubstringCount("bcca", "abc"))
    print(solution.validSubstringCount("abcabc", "abc"))
    print(solution.validSubstringCount("abcabc", "aaabc"))
