class Solution:
    def countRotations(self, s: str, k: int) -> int:
        ans = cnt = 0
        n = len(s)
        for i in range(n + k):
            if s[i] == s[i + 1]:
                cnt += 1
            left = i - k + 1
            if left < 0:
                continue
            