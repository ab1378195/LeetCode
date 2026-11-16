class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        has = {}
        for i, num in enumerate(nums):
            if num in has and i - has[num] <= k:
                return True
            has[num] = i
        return False


if __name__ == "__main__":
    solution = Solution()
    print(solution.containsNearbyDuplicate([1, 2, 3, 1], 3))
    print(solution.containsNearbyDuplicate([1, 0, 1, 1], 1))
    print(solution.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))
