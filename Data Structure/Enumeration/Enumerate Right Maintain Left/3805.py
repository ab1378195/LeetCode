from typing import List
from collections import defaultdict


class Solution:
    def countPairs(self, words: List[str]) -> int:
        cnt = defaultdict(int)
        ans = 0
        for word in words:
            ascii_list = list(map(ord, word))
            key = tuple(map(lambda ascii: (ascii - ascii_list[0]) % 26, ascii_list))
            ans += cnt[key]
            cnt[key] += 1
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.countPairs(["fusion", "layout"]))
    print(solution.countPairs(["ab", "aa", "za", "aa"]))
