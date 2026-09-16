from typing import List


class Solution:
    def maxSatisfied(
        self, customers: List[int], grumpy: List[int], minutes: int
    ) -> int:
        # grumpy分为0,1两种情况,使用长度为2的s就可以省去if简化统计
        s = [0, 0]
        ans = 0
        for i, (customer, g) in enumerate(zip(customers, grumpy)):
            s[g] += customer
            left = i - minutes + 1
            if left < 0:
                continue
            ans = max(ans, s[1])
            if grumpy[left]:
                s[1] -= customers[left]
        return ans + s[0]


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxSatisfied([1, 0, 1, 2, 1, 1, 7, 5], [0, 1, 0, 1, 0, 1, 0, 1], 3))
    print(solution.maxSatisfied([1], [0], 1))
