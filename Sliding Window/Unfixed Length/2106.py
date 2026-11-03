from bisect import bisect_left


class Solution:
    def maxTotalFruits(self, fruits: list[list[int]], startPos: int, k: int) -> int:
        left = bisect_left(fruits, [startPos - k])
        right = bisect_left(fruits, [startPos + 1])
        ans = s = sum(fruit[1] for fruit in fruits[left:right])
        while right < len(fruits) and fruits[right][0] <= startPos + k:
            s += fruits[right][1]
            while (
                fruits[right][0] * 2 - fruits[left][0] - startPos > k
                and fruits[right][0] - fruits[left][0] * 2 + startPos > k
            ):
                s -= fruits[left][1]
                left += 1
            ans = max(ans, s)
            right += 1
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxTotalFruits([[2, 8], [6, 3], [8, 6]], 5, 4))
    print(
        solution.maxTotalFruits([[0, 9], [4, 1], [5, 7], [6, 2], [7, 4], [10, 9]], 5, 4)
    )
    print(solution.maxTotalFruits([[0, 3], [6, 4], [8, 5]], 3, 2))
