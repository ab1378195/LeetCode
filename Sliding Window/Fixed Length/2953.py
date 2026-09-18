from collections import Counter


class Solution:
    def countCompleteSubstrings(self, word: str, k: int) -> int:
        def f(s: str) -> int:
            res = 0
            # 枚举子串中有m种字母
            for m in range(1, 27):
                size = m * k
                if size > len(s):
                    break
                cnt = Counter(s[:size])
                # 双重哈希
                cc = Counter(cnt.values())
                # 若出现次数为k的字母有m种,则符合条件
                if cc[k] == m:
                    res += 1
                for in_, out in zip(s[size:], s):
                    # 将in_的出现次数从一组删去然后移到另一组
                    cc[cnt[in_]] -= 1
                    cnt[in_] += 1
                    cc[cnt[in_]] += 1

                    cc[cnt[out]] -= 1
                    cnt[out] -= 1
                    cc[cnt[out]] += 1

                    if cc[k] == m:
                        res += 1
            return res

        n = len(word)
        ans = i = 0
        while i < n:
            start = i
            i += 1
            while i < n and abs(ord(word[i]) - ord(word[i - 1])) <= 2:
                i += 1
            ans += f(word[start:i])
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.countCompleteSubstrings("igigee", 2))
    print(solution.countCompleteSubstrings("aaabbbccc", 3))
