class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            temp = 0
            new_s = ""
            for i, ch in enumerate(s):
                temp += int(ch)
                if (i + 1) % k == 0:
                    new_s += str(temp)
                    temp = 0
            if (i + 1) % k != 0:
                s = new_s + str(temp)
            else:
                s = new_s
        return s


if __name__ == "__main__":
    solution = Solution()
    print(solution.digitSum("11111222223", 3))
    print(solution.digitSum("00000000", 3))
    print(solution.digitSum("1234", 2))
