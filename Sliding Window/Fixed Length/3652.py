from typing import List


class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        # 对于要计算修改后窗口内值和未被修改值总和的情况,将滑窗的统计值定义为增量,则可以在一次遍历内完成对所有元素的统计和滑窗的统计
        total = extra = max_extra = 0
        m = k // 2
        for i, (price, operation) in enumerate(zip(prices, strategy)):
            total += price * operation
            if i < m:
                continue
            extra -= prices[i - m] * strategy[i - m]
            extra += (1 - operation) * price
            left = i - k + 1
            if left < 0:
                continue
            max_extra = max(max_extra, extra)
            extra += strategy[left] * prices[left]
            extra -= (1 - strategy[left + m]) * prices[left + m]
        return total + max_extra


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxProfit([4, 2, 8], [-1, 0, 1], 2))
    print(solution.maxProfit([5, 4, 3], [1, 1, 0], 2))
