from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        threshold *= k
        sum = 0
        ans = 0
        for i, num in enumerate(arr):
            sum += num
            left = i - k + 1
            if left < 0:
                continue
            if sum >= threshold:
                ans += 1
            sum -= arr[left]
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.numOfSubarrays([2, 2, 2, 2, 5, 5, 5, 8], 3, 4))
    print(solution.numOfSubarrays([11, 13, 17, 23, 29, 31, 7, 5, 2, 3], 3, 5))
