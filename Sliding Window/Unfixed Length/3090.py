from collections import defaultdict

class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        cnt = defaultdict(int)
        ans = left = 0
        for right, c in enumerate(s):
            cnt[c]+=1
            while cnt[c]>2:
                cnt[s[left]]-=1
                left+=1
            ans = max(ans, right-left+1)
        return ans

if __name__ =="__main__":
    solution = Solution()
    print(solution.maximumLengthSubstring("bcbbbcba"))
    print(solution.maximumLengthSubstring("aaaa"))