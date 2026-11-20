from typing import List


class Solution:
    """定义f[x]表示子序列最后一个数为x时的最大子序列长度,f0,f1,f2分别表示f[x-1],f[x],f[x+1]"""

    def maxSelectedElements(self, nums: List[int]) -> int:
        nums.sort()
        ans = pre = f0 = f1 = f2 = 0
        for num in nums:
            # num是当前处理的x,pre是前一个处理的x
            if num == pre + 1:
                f0 = f1
                f1 = f2
            elif num == pre + 2:
                f0 = f2
                f1 = 0
            elif num > pre + 2:
                f0 = 0
                f1 = 0

            f2 = f1 + 1
            f1 = f0 + 1
            ans = max(ans, f1, f2)
            pre = num
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxSelectedElements([2, 1, 5, 1, 1]))
    print(solution.maxSelectedElements([1, 4, 7, 10]))
