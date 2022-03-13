"""
Two Sum II

Given an array of integers numbers that is already sorted in non-decreasing 
order, find two numbers such that they add up to a specific target number. 
Let these two numbers be numbers[index1] and numbers[index2] where 
0 <= index1 < index2 < numbers.length.

Return the indices of the two numbers, index1 and index2 as an integer array 
[index1, index2] of length 2.

You may not use the same element twice.

Your solution must use only constant extra space. i.e. O(1) Space Complexity

Example 1:
Input: numbers = [2,7,11,15], target = 9 Output: [0,1] Explanation: 
The sum of 2 and 7 is 9. Therefore, index1 = 0, index2 = 1. We return [0, 1].

Example 2:
Input: numbers = [2,3,4], target = 6 Output: [0,2] Explanation: 
The sum of 2 and 4 is 6. Therefore index1 = 0, index2 = 2. We return [0, 2].

Example 3:
Input: numbers = [-1,0], target = -1 Output: [0, 1] Explanation: 
The sum of -1 and 0 is -1. Therefore index1 = 0, index2 = 1. We return [0, 1]."""

def two_sum(nums, k):
    left = 0
    right = len(nums) - 1 

    while left < right: 
        total = nums[left] + nums[right]

        if total == k:
            return [left, right]
        elif total < k:
            left += 1
        elif total > k:
            right -= 1

    return None


if __name__ == '__main__':
    assert two_sum([1, 2, 3, 4, 5], 6) == [0, 4]
    assert two_sum([1, 2, 3, 4, 5], 2) == None
    assert two_sum([2, 3, 4, 5], 3) == None
    assert two_sum([1, 2, 3, 4, 5], 45) == None
    assert two_sum([1, 2, 3, 4, 5], 7) == [1, 4]


    
