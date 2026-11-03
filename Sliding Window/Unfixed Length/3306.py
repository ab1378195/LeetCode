from collections import defaultdict


class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        ans = 0
        left1 = left2 = 0
        cnt1 = defaultdict(int)
        cnt2 = defaultdict(int)
        less1 = less2 = 5
        consonants1 = consonants2 = 0
        for right, ch in enumerate(word):
            if ch not in "aeiou":
                consonants1 += 1
                consonants2 += 1
            else:
                cnt1[ch] += 1
                if cnt1[ch] == 1:
                    less1 -= 1
                cnt2[ch] += 1
                if cnt2[ch] == 1:
                    less2 -= 1
            while less1 == 0 and consonants1 >= k:
                out = word[left1]
                if out not in "aeiou":
                    consonants1 -= 1
                else:
                    cnt1[out] -= 1
                    if cnt1[out] == 0:
                        less1 += 1
                left1 += 1
            while less2 == 0 and consonants2 > k:
                out = word[left2]
                if out not in "aeiou":
                    consonants2 -= 1
                else:
                    cnt2[out] -= 1
                    if cnt2[out] == 0:
                        less2 += 1
                left2 += 1
            ans += left1 - left2
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.countOfSubstrings("aeioqq", 1))
    print(solution.countOfSubstrings("aeiou", 0))
    print(solution.countOfSubstrings("ieaouqqieaouqq", 1))
