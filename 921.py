class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        cnt = 0
        ans = 0
        for c in s:
            if c == "(":
                cnt += 1
            else:
                cnt -= 1
                if cnt < 0:
                    cnt += 1
                    ans += 1
        return ans + cnt


if __name__ == "__main__":
    solution = Solution()
    print(solution.minAddToMakeValid("())"))
    print(solution.minAddToMakeValid("((("))
