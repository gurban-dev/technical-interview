"""
Given an integer array nums, return true if any
value appears more than once in the array,
otherwise return false.

Algorithm

Input:
An integer array called "nums".

Output:
True or false depending on whether the
array called "nums" contains a duplicate
value.

A set is a data structure in Python that
stores unique values.

1. Declare a container of type "set" called
   "unique_values".
2. Loop through the elements inside the "nums"
   array.
   a. If the current element is already inside
      "unique_values", return False.
      Otherwise, add the current element to
      "unique_values".
   b. Continue to the next iteration.
3. Return true, as a duplicate was never detected
   while looping through the elements of "nums".
"""

def has_duplicate(nums: list[int]) -> bool:
  if not nums:
    return False

  unique_values = set()

  for num in nums:
    if num in unique_values:
      return True

    unique_values.add(num)

  return False

print(f'has_duplicate([1, 2, 3, 3]): {has_duplicate([1, 2, 3, 3])}')

print(f'\nhas_duplicate([1, 2, 3, 4]): {has_duplicate([1, 2, 3, 4])}')