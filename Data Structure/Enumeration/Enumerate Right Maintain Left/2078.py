from typing import List


class Solution:
    """注意贪心思想的使用,colors[0]或colors[n-1]必然参与最大值的计算"""

    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        c = colors[0]
        if c != colors[n - 1]:
            return n - 1

        # 基于colors[0]找最右的
        for right in range(n - 2, 0, -1):
            if colors[right] != c:
                break

        # 基于colors[n-1]找最左的
        for left in range(1, n - 1):
            if colors[left] != c:
                break
        return max(right, n - 1 - left)


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxDistance([1, 1, 1, 6, 1, 1, 1]))
    print(solution.maxDistance([1, 8, 3, 8, 3]))
    print(solution.maxDistance([0, 1]))
