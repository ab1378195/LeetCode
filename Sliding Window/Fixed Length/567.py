from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m = len(s1)
        if m > len(s2):
            return False
        cnt = Counter(s1)
        less = len(cnt)
        for i, c in enumerate(s2):
            cnt[c] -= 1
            if cnt[c] == 0:
                less -= 1
            left = i - m + 1
            if left < 0:
                continue
            if less == 0:
                return True
            out = s2[left]
            if cnt[out] == 0:
                less += 1
            cnt[out] += 1
        return False


if __name__ == "__main__":
    solution = Solution()
    print(solution.checkInclusion("ab", "eidbaooo"))
    print(solution.checkInclusion("hello", "ooolleoooleh"))
