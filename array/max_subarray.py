def find_max_sub_array(nums: list[int]) -> int:
  # Subarray with the largest sum.
  max_subarray: int = nums[0]

  # sum_of_current_subarray keeps track of the sum of the current subarray.
  sum_of_current_subarray = 0

  for num in nums:
    # If sum_of_current_subarray becomes negative, then including
    # it in any future subarray would only make the sum smaller.

    # So when sum_of_current_subarray < 0, you "throw away" the
    # subarray so far and start fresh at the next element.
    if sum_of_current_subarray < 0:
      sum_of_current_subarray = 0

    sum_of_current_subarray += num
    
    max_subarray = max(sum_of_current_subarray, max_subarray)
  return max_subarray

print('find_max_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4]):',
      find_max_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4]))

# Input: [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6

'''
This solution is known as Kadane's algorithm.

Start:  sum_of_current_subarray = 0
nums:   [-2] -> sum_of_current_subarray = -2   (reset next step)
nums:   [1]  -> sum_of_current_subarray = 1
nums:   [1,-3] -> sum_of_current_subarray = -2 (reset next step)
nums:   [4]  -> sum_of_current_subarray = 4
nums:   [4,-1] -> sum_of_current_subarray = 3
nums:   [4,-1,2] -> sum_of_current_subarray = 5
nums:   [4,-1,2,1] -> sum_of_current_subarray = 6  ✅ peak
nums:   [4,-1,2,1,-5] -> sum_of_current_subarray = 1
nums:   [4,-1,2,1,-5,4] -> sum_of_current_subarray = 5
'''