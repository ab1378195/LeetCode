from collections import Counter
from math import inf


class Solution:
    def balancedString(self, s: str) -> int:
        m = len(s) // 4
        cnt = Counter(s)
        if len(cnt) == 4 and min(cnt.values()) == m:
            return 0
        ans, left = inf, 0
        for right, ch in enumerate(s):
            # 统计窗口外字母个数,当字母个数均不超过m,替换当前窗口可使字符串符合要求
            cnt[ch] -= 1
            while max(cnt.values()) <= m:
                ans = min(ans, right - left + 1)
                cnt[s[left]] += 1
                left += 1
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.balancedString("QWER"))
    print(solution.balancedString("QQWE"))
    print(solution.balancedString("QQQW"))
    print(solution.balancedString("QQQQ"))
