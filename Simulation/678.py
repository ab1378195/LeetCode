class Solution:
    def checkValidString(self, s: str) -> bool:
        cnt_min = cnt_max = 0
        for c in s:
            if c == "(":
                cnt_max += 1
                cnt_min += 1
            elif c == ")":
                cnt_max -= 1
                cnt_min -= 1
                if cnt_max < 0:
                    return False
            else:
                cnt_max += 1
                cnt_min -= 1
            cnt_min = max(cnt_min, 0)
        return cnt_min == 0


if __name__ == "__main__":
    solution = Solution()
    print(solution.checkValidString("()"))
    print(solution.checkValidString("(*)"))
    print(solution.checkValidString("(*))"))
