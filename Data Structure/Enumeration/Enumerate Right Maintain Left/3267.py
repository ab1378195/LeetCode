from typing import List
from collections import defaultdict

POW10 = [10**i for i in range(7)]


class Solution:
    def countPairs(self, nums: List[int]) -> int:
        nums.sort()
        cnt = defaultdict(int)
        ans = 0
        for num in nums:
            st = {num}
            # 把num数位上的数字拆开,低位放左边
            a = list(map(int, str(num)))[::-1]
            m = len(a)
            for i in range(m):
                for j in range(i + 1, m):
                    if a[i] == a[j]:
                        continue
                    y = num + (a[j] - a[i]) * (POW10[i] - POW10[j])
                    st.add(y)  # 交换一次
                    a[i], a[j] = a[j], a[i]
                    for p in range(i + 1, m):
                        for q in range(p + 1, m):
                            st.add(
                                y + (a[q] - a[p]) * (POW10[p] - POW10[q])
                            )  # 交换第二次
                    a[i], a[j] = a[j], a[i]
            ans += sum(cnt[v] for v in st)
            cnt[num] += 1
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.countPairs([1023, 2310, 2130, 213]))
    print(solution.countPairs([1, 10, 100]))
