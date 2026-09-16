from collections import defaultdict


class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        str_cnt = defaultdict(int)
        char_cnt = defaultdict(int)
        for i, c in enumerate(s):
            char_cnt[c] += 1
            left = i - minSize + 1
            if left < 0:
                continue
            if len(char_cnt) <= maxLetters:
                str_cnt[s[left : i + 1]] += 1
            out = s[left]
            char_cnt[out] -= 1
            if char_cnt[out] == 0:
                del char_cnt[out]
        return max(str_cnt.values(), default=0)


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxFreq("aababcaab", 2, 3, 4))
    print(solution.maxFreq("aaaa", 1, 3, 3))
