from typing import List


class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr1.sort()
        arr2.sort()
        ans = i = 0
        for num in arr1:
            while i < len(arr2) and arr2[i] < num - d:
                i += 1
            if i == len(arr2) or arr2[i] > num + d:
                ans += 1
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.findTheDistanceValue([4, 5, 8], [10, 9, 1, 8], 2))
    print(solution.findTheDistanceValue([1, 4, 2, 3], [-4, -3, 6, 10, 20, 30], 3))
    print(solution.findTheDistanceValue([2, 1, 100, 3], [-5, -2, 10, -3, 7], 6))
