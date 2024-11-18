"""https://leetcode.com/problems/
arithmetic-slices/submissions/1456052941"""

from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0

        count = 0
        # sum = nums[0]+nums[1]+nums[2]
        # isMonotonn = nums[0]-nums[1]==nums[1]-nums[2]
        # arith_sum = (nums[0]+nums[2])*3//2
        # if isMonotonn and arith_sum==sum: count+=1
        # start = 0
        # end = 3
        # flagEnd = False
        # flag = False
        # while end<len(nums):
        #     if not flagEnd: sum+=nums[end]
        #     else: flagEnd = False
        #     if end-start+1>3:
        #         isMonotonn = isMonotonn and nums[end]-nums[end-1]==nums[start+1]-nums[start]
        #     else: isMonotonn = nums[end]-nums[end-1]==nums[start+1]-nums[start]
        #     if not isMonotonn:
        #         if end-start+1==3: end+=1
        #         else: flagEnd = True
        #         start+=1
        #         sum-=nums[start-1]

        #         continue
        #     arith_sum = (nums[start]+nums[end])*(end-start+1)//2
        #     if not flag and sum==arith_sum: count+=1
        #     elif flag: flag = False
        #     end+=1
        #     if end==len(nums):
        #         start+=1
        #         end = start+2
        #         if end>=len(nums): break
        #         isMonotonn = nums[start]-nums[start+1]==nums[start+1]-nums[end]
        #         sum = nums[start]+nums[start+1]+nums[end]
        #         arith_sum = (nums[start]+nums[end])*3//2
        #         if isMonotonn and arith_sum==sum: count+=1
        #         if end==len(nums)-1:break
        #         flagEnd = True
        #         flag = True

        for i in range(len(nums) - 2):
            sum = nums[i] + nums[i + 1]
            isMonotonn = nums[i + 1] - nums[i] == nums[i + 2] - nums[i + 1]
            if isMonotonn:
                dif = nums[i + 1] - nums[i]
                for j in range(i + 2, len(nums)):
                    sum += nums[j]
                    arith_sum = (nums[i] + nums[j]) * (j - i + 1) // 2
                    if j != i + 2:
                        isMonotonn = isMonotonn and nums[j] - nums[j - 1] == dif
                    if not isMonotonn:
                        break
                    elif sum == arith_sum:
                        count += 1

        return count


a = Solution()
print(a.numberOfArithmeticSlices([1, 2, 3, 4, 8, 9, 10]))
