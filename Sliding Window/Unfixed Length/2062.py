from collections import defaultdict


class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        cnt = defaultdict(int)
        left = ans = start = 0
        for right, ch in enumerate(word):
            if ch not in "aeiou":
                start = left = right + 1
                cnt.clear()
                continue
            cnt[ch] += 1
            while len(cnt) == 5:
                out = word[left]
                if cnt[out] == 1:
                    del cnt[out]
                else:
                    cnt[out] -= 1
                left += 1
            ans += left - start
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.countVowelSubstrings("aeiouu"))
    print(solution.countVowelSubstrings("unicornarihan"))
    print(solution.countVowelSubstrings("cuaieuouac"))
    print(solution.countVowelSubstrings("bbaeixoubb"))
