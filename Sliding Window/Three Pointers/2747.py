from typing import List


class Solution:
    def countServers(
        self, n: int, logs: List[List[int]], x: int, queries: List[int]
    ) -> List[int]:
        logs.sort(key=lambda log: log[1])
        idx = sorted(range(len(queries)), key=lambda i: queries[i])
        cnt = [0] * (n + 1)
        not_receives = n
        left = right = 0

        for qid in idx:
            query = queries[qid]
            while right < len(logs) and logs[right][1] <= query:
                i = logs[right][0]
                if cnt[i] == 0:
                    not_receives -= 1
                cnt[i] += 1
                right += 1

            while left < len(logs) and logs[left][1] < query - x:
                i = logs[left][0]
                cnt[i] -= 1
                if cnt[i] == 0:
                    not_receives += 1
                left += 1

            queries[qid] = not_receives
        return queries


if __name__ == "__main__":
    solution = Solution()
    print(solution.countServers(3, [[1, 3], [2, 6], [1, 5]], 5, [10, 11]))
    print(solution.countServers(3, [[2, 4], [2, 1], [1, 2], [3, 1]], 2, [3, 4]))
