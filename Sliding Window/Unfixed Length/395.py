from collections import Counter


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        ans = 0
        for p in range(1, 27):
            cnt = Counter()
            left = 0
            tot = 0  # 窗口有多少种不同字符
            less = 0  # 窗口中次数小于k的种类
            for right, num in enumerate(s):
                cnt[num] += 1
                # 由于k可能为1,因此注意判断1和k的顺序
                if cnt[num] == 1:
                    tot += 1
                    less += 1
                if cnt[num] == k:
                    less -= 1
                while tot > p:
                    if cnt[s[left]] == k:
                        less += 1
                    if cnt[s[left]] == 1:
                        less -= 1
                        tot -= 1
                    cnt[s[left]] -= 1
                    left += 1
                if less == 0:
                    ans = max(ans, right - left + 1)
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.longestSubstring("aaabb", 3))
    print(solution.longestSubstring("ababbc", 2))
