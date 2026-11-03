from collections import defaultdict


class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        ans = ""
        for ch_kind in range(1, 27):
            cnt_lower = defaultdict(int)
            cnt_upper = defaultdict(int)
            left = 0
            cnt = 0  # 未配对数目
            for right, ch in enumerate(s):
                # 大写字母
                if ord(ch) < ord("a"):
                    key = ord(ch) - ord("A")
                    if cnt_upper[key] == 0:
                        if cnt_lower[key] == 0:
                            cnt += 1
                        else:
                            cnt -= 1
                    cnt_upper[key] += 1
                # 小写字母
                else:
                    key = ord(ch) - ord("a")
                    if cnt_lower[key] == 0:
                        if cnt_upper[key] == 0:
                            cnt += 1
                        else:
                            cnt -= 1
                    cnt_lower[key] += 1
                while max(len(cnt_lower), len(cnt_upper)) > ch_kind:
                    # 大写字母
                    if ord(s[left]) < ord("a"):
                        key = ord(s[left]) - ord("A")
                        cnt_upper[key] -= 1
                        if cnt_upper[key] == 0:
                            if cnt_lower[key] == 0:
                                cnt -= 1
                                del cnt_lower[key]
                                del cnt_upper[key]
                            else:
                                cnt += 1

                    # 小写字母
                    else:
                        key = ord(s[left]) - ord("a")
                        cnt_lower[key] -= 1
                        if cnt_lower[key] == 0:
                            if cnt_upper[key] == 0:
                                cnt -= 1
                                del cnt_lower[key]
                                del cnt_upper[key]
                            else:
                                cnt += 1
                    left += 1
                if cnt == 0:
                    if right - left + 1 > len(ans):
                        ans = s[left : right + 1]
            cnt_lower.clear()
            cnt_upper.clear()
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.longestNiceSubstring("YazaAay"))
    print(solution.longestNiceSubstring("Bb"))
    print(solution.longestNiceSubstring("c"))
    print(solution.longestNiceSubstring("dDzeE"))
