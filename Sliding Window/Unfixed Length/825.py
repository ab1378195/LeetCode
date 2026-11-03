class Solution:
    def numFriendRequests(self, ages: list[int]) -> int:
        cnt = [0] * 121
        for age in ages:
            cnt[age] += 1
        ans = cnt_window = age_y = 0
        for age_x, c in enumerate(cnt):
            cnt_window += c
            if age_y * 2 <= age_x + 14:
                cnt_window -= cnt[age_y]
                age_y += 1
            if cnt_window:
                ans += c * cnt_window - c
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.numFriendRequests([16, 16]))
    print(solution.numFriendRequests([16, 17, 18]))
    print(solution.numFriendRequests([20, 30, 100, 110, 120]))
