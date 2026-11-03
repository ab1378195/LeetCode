class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        left = ans = 0
        cnt_zero = 0
        cnt_one = 0
        for right, ch in enumerate(s):
            if ch == "1":
                cnt_one += 1
            else:
                cnt_zero += 1
            while min(cnt_zero, cnt_one) > k:
                if s[left] == "1":
                    cnt_one -= 1
                else:
                    cnt_zero -= 1
                left += 1
            ans += right - left + 1
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.countKConstraintSubstrings("10101", 1))
    print(solution.countKConstraintSubstrings("1010101", 2))
    print(solution.countKConstraintSubstrings("11111", 1))
