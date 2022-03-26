"""
Given an integer array nums, return all the triplets 
[nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k,
and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Input: nums = []
Output: []

Input: nums = [0]
Output: []

k = 0
current_target = k - 1
target = current target - cur

[-1, 0, 1, 2, -1, -4]
[-4, -1, -1, 0, 1, 2]
"""


def three_sum(nums):
    nums.sort()

    result = []
    
    for i, val in enumerate(nums):
        if i > 0 and val == nums[i - 1]:
            continue

        l = i + 1
        r = len(nums) - 1

        while l < r:
            total = nums[i] + nums[l] + nums[r]
            if total < 0:
                l += 1
            elif total > 0:
                r -= 1
            else:
                result.append([nums[i], nums[l], nums[r]])
                l += 1
                while nums[l] == nums[l - 1] and l < r:
                        l += 1

    return result
