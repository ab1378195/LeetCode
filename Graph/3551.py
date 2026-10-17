from typing import List


class Solution:
    """把元素在排序前数组的下标和排序后数组的下标连起来,构造出图,图中每个长度为k的环就代表要执行k-1次交换。
    将所有的k_i-1加起来得到sum(k)-m,其中sum(k)=len(nums),m=环(连通块)的个数
    """

    def minSwaps(self, nums: List[int]) -> int:
        a = sorted([sum(map(int, str(x))), x, i] for i, x in enumerate(nums))
        cc = 0
        for _, _, i in a:
            if i < 0:
                continue
            cc += 1
            while i >= 0:
                temp = i
                i = a[i][2]
                a[temp][2] = -1
        return len(a) - cc


if __name__ == "__main__":
    solution = Solution()
    print(solution.minSwaps([37, 100]))
    print(solution.minSwaps([22, 14, 33, 7]))
    print(solution.minSwaps([18, 43, 34, 16]))
