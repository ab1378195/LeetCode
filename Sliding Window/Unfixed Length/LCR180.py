from typing import List


class Solution:
    def fileCombination(self, target: int) -> List[List[int]]:
        ans = []
        s = 0
        left = 1
        for num in range(1, target // 2 + 2):
            s += num
            while s > target:
                s -= left
                left += 1
            if s == target and left < num:
                ans.append(list(range(left, num + 1)))
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.fileCombination(12))
    print(solution.fileCombination(18))
    print(solution.fileCombination(1))
