class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        odd = s = 0
        for num in arr:
            s += num
            odd += s & 1
        return odd * (len(arr) + 1 - odd) % 1_000_000_007


if __name__ == "__main__":
    solution = Solution()
    print(solution.numOfSubarrays([1, 3, 5]))
    print(solution.numOfSubarrays([2, 4, 6]))
    print(solution.numOfSubarrays([1, 2, 3, 4, 5, 6, 7]))
    print(solution.numOfSubarrays([100, 100, 99, 99]))
    print(solution.numOfSubarrays([7]))
