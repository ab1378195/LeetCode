from typing import List


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        ans = max_diff = pre_max = 0
        for num in nums:
            ans = max(ans, max_diff * num)
            max_diff = max(max_diff, pre_max - num)
            pre_max = max(pre_max, num)
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.maximumTripletValue([12, 6, 1, 2, 7]))
    print(solution.maximumTripletValue([1, 10, 3, 4, 19]))
    print(solution.maximumTripletValue([1, 2, 3]))
