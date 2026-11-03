class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        left = ans = 0
        cnt = [0, 0, 0]
        less = 3
        for right, ch in enumerate(s):
            key = ord(ch) - ord("a")
            cnt[key] += 1
            if cnt[key] == 1:
                less -= 1
            while less == 0:
                key = ord(s[left]) - ord("a")
                cnt[key] -= 1
                if cnt[key] == 0:
                    less += 1
                left += 1
            ans += left
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.numberOfSubstrings("abcabc"))
    print(solution.numberOfSubstrings("aaacb"))
    print(solution.numberOfSubstrings("abc"))
