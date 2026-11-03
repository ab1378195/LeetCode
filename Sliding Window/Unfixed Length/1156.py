from collections import defaultdict, Counter


class Solution:
    def maxRepOpt1(self, text: str) -> int:
        cnt_total = Counter(text)
        cnt = defaultdict(int)
        left = mx = 0
        for right, ch in enumerate(text):
            cnt[ch] += 1
            if cnt_total[ch] > cnt[ch] > mx:
                mx = cnt[ch]
            if right - left + 1 - mx > 1:
                cnt[text[left]] -= 1
                left += 1
        return len(text) - left


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxRepOpt1("ababa"))
    print(solution.maxRepOpt1("aaabaaa"))
    print(solution.maxRepOpt1("aaabbaaa"))
    print(solution.maxRepOpt1("aaaaa"))
    print(solution.maxRepOpt1("abcdef"))
