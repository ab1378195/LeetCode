from itertools import pairwise


class Solution:
    def countRotations(self, s: str, k: int) -> int:
        n = len(s)
        cnt = 1 if s[0] == s[-1] else 0
        for x, y in pairwise(s):
            if x == y:
                cnt += 1
        if cnt == k:
            return n - cnt
        if cnt == k + 1:
            return cnt
        return 0


if __name__ == "__main__":
    solution = Solution()
    print(solution.countRotations("aab", 1))
    print(solution.countRotations("abca", 0))
