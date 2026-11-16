class Solution:
    """可以将循环中的更新变为ans在前,cnt在后,这样循环可以从n-1开始且不用专门初始化cnt"""

    def countOppositeParity(self, nums: list[int]) -> list[int]:
        n = len(nums)
        # cnt用于统计奇偶数的数量,0为偶数,1为奇数
        if nums[n - 1] & 1:
            cnt = [0, 1]
        else:
            cnt = [1, 0]
        ans = [0] * n
        for i in range(n - 2, -1, -1):
            isEven = nums[i] & 1
            ans[i] += cnt[isEven ^ 1]
            cnt[isEven] += 1
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.countOppositeParity([1, 2, 3, 4]))
    print(solution.countOppositeParity([1]))
