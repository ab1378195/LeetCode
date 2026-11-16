class Solution:
    def canArrange(self, arr: list[int], k: int) -> bool:
        cnt = [0] * k
        match = 0
        for num in arr:
            remainder = (k - num % k) % k
            if cnt[remainder] > 0:
                match += 1
                cnt[remainder] -= 1
            else:
                cnt[num % k] += 1
        return match == len(arr) // 2


if __name__ == "__main__":
    solution = Solution()
    print(solution.canArrange([1, 2, 3, 4, 5, 10, 6, 7, 8, 9], 5))
    print(solution.canArrange([1, 2, 3, 4, 5, 6], 7))
    print(solution.canArrange([1, 2, 3, 4, 5, 6], 10))
