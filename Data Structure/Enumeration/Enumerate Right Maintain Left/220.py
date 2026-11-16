class Solution:
    def containsNearbyAlmostDuplicate(
        self, nums: list[int], indexDiff: int, valueDiff: int
    ) -> bool:
        buckets = {}
        bucket_size = valueDiff + 1
        for i, num in enumerate(nums):
            if i > indexDiff:
                out_index = nums[i - indexDiff - 1] // bucket_size
                if out_index in buckets:
                    del buckets[out_index]
            cur_index = num // bucket_size
            if cur_index in buckets:
                return True
            if (
                cur_index - 1 in buckets
                and abs(num - buckets[cur_index - 1]) <= valueDiff
            ):
                return True
            if (
                cur_index + 1 in buckets
                and abs(num - buckets[cur_index + 1]) <= valueDiff
            ):
                return True
            buckets[cur_index] = num
        return False


if __name__ == "__main__":
    solution = Solution()
    print(solution.containsNearbyAlmostDuplicate([1, 2, 3, 1], 3, 0))
    print(solution.containsNearbyAlmostDuplicate([1, 5, 9, 1, 5, 9], 2, 3))
