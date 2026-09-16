class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        count = 0
        ans = 0
        for i, c in enumerate(s):
            if c in "aeiou":
                count += 1
            left = i - k + 1
            if left < 0:
                continue
            ans = max(ans, count)
            if s[left] in "aeiou":
                count -= 1
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxVowels("abciiidef", 3))
    print(solution.maxVowels("aeiou", 2))
    print(solution.maxVowels("leetcode", 3))
