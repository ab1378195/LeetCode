from typing import List


class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        # 全初始化为-1,就不用像分段函数一样考虑该问题,更简化
        ans = [-1] * len(nums)
        s = 0
        dividor = 2 * k + 1
        for i, num in enumerate(nums):
            s += num
            if i < 2 * k:
                continue
            ans[i - k] = s // dividor
            s -= nums[i - k * 2]
        return ans

if __name__ == "__main__":
    solution = Solution()
    print(solution.getAverages([7, 4, 3, 9, 1, 8, 5, 2, 6], 3))
    print(solution.getAverages([100000], 0))
    print(solution.getAverages([8], 100000))
