#https://leetcode.com/problems/3sum-closest/
#Given an integer array nums of length n and an integer target, 
# find three integers in nums such that the sum is closest to target.
#Return the sum of the three integers.
#You may assume that each input would have exactly one solution.
#Input: nums = [-1,2,1,-4], target = 1
#Output: 2
#Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
sorted(list(map(lambda n: [n,sum(n)],[nums[i:i+3]for i in range(len((nums))-(3-1)+1)])),key=lambda n: n[1])
[[[1, -4], -3], [[2, 1, -4], -1], [[-1, 2, 1], 2]]