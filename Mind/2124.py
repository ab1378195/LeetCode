class Solution:
    """实际上本题的充要条件是检查字符串中是否有ba出现"""

    def checkString(self, s: str) -> bool:
        b_exist = False
        for ch in s:
            if ch == "b":
                b_exist = True
            else:
                if b_exist:
                    return False
        return True


if __name__ == "__main__":
    solution = Solution()
    print(solution.checkString("aaabbb"))
    print(solution.checkString("abab"))
    print(solution.checkString("bbb"))
