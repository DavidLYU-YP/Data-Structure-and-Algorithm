class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        ans = {}
        for i in range(len(nums)):
            if nums[i] not in ans:
                ans[nums[i]] = [0, i, 0]
            ans[nums[i]][0] += 1
            ans[nums[i]][2] = i

        maxnum = minlen = 0
        for num, left, right in ans.values():
            if num > maxnum:
                maxnum = num
                minlen = right - left +1
            elif num == maxnum:
                if right - left +1 < minlen:
                    minlen = right - left +1

        return minlen