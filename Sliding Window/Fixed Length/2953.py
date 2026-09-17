from collections import defaultdict


class Solution:
    def countCompleteSubstrings(self, word: str, k: int) -> int:
        ans = 0
        cnt = defaultdict(int)
        cnt[word[0]] += 1
        left = 0
        right = 1
        in_val = last_val = ord(word[0]) & 31
        while right < len(word):
            while abs(last_val - in_val) > 2:
                in_word = word[right]
                in_val = ord(in_word) & 31
                cnt[in_word] += 1
                right += 1
                out_word = word[left]
                cnt[out_word] -= 1
                left += 1
                last_val = in_val
