from collections import Counter, defaultdict
from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        # 本质上是把每个单词看作了一个元素,注意步长和统计口径
        word_len = len(words[0])
        window_len = word_len * len(words)
        target_cnt = Counter(words)
        ans = []
        for start in range(word_len):
            cnt = defaultdict(int)
            overload = 0
            for right in range(start + word_len, len(s) + 1, word_len):
                in_word = s[right - word_len : right]
                if cnt[in_word] == target_cnt[in_word]:
                    overload += 1
                cnt[in_word] += 1
                left = right - window_len
                if left < 0:
                    continue
                if overload == 0:
                    ans.append(left)
                out_word = s[left : left + word_len]
                cnt[out_word] -= 1
                if cnt[out_word] == target_cnt[out_word]:
                    overload -= 1
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.findSubstring("barfoothefoobarman", ["foo", "bar"]))
    print(
        solution.findSubstring(
            "wordgoodgoodgoodbestword", ["word", "good", "best", "word"]
        )
    )
    print(solution.findSubstring("barfoofoobarthefoobarman", ["bar", "foo", "the"]))
