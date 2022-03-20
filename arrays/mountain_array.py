"""
Given an array of integers arr, return true if and only if it 
is a valid mountain array.

"""

def is_mountain_array(nums):
    if len(nums) < 3:
        return False
    
    l = 0
    r = len(nums) - 1

    while l < len(nums) - 1:
        left_slope = nums[l+1] - nums[l]

        if left_slope > 0:
            l += 1
        else:
            break

    while r > 1:
        right_slope = nums[r-1] - nums[r]

        if right_slope > 0:
            r -= 1
        else:
            break

    if l == r and l != len(nums) - 1:
        return True
    return False

assert is_mountain_array([0, 1, 2, 3, 2, 0]) == True
assert is_mountain_array([0, 1, 3, 3, 2, 0]) == False
assert is_mountain_array([0, 1, 2, 3, 2, 5]) == False
assert is_mountain_array([0, 1, 2, 2, 2, 0]) == False
assert is_mountain_array([0, 1, 2, 3, 4, 5]) == False
assert is_mountain_array([5, 4, 3, 1]) == False