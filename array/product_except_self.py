# Prefix + Postfix Pattern

'''
1. Initialise a list named "result" that is the same size as
   the input array, filled with 1s. Also set prefix = 1 and
   postfix = 1.

2. Forward pass (prefix): Traverse the array from left to right.
   At each index, set result[index] to prefix, then update
   prefix *= nums[index].
   
3. Backward pass (postfix): Traverse the array from right to left.
   At each index, multiply result[index] by postfix, then update
   postfix *= nums[index].
'''

def product_except_self(arr: list[int]) -> list[int]:
  result = [1] * len(arr)

  # result = [1 for i in range(len(arr))]

  prefix = 1

  for index in range(len(arr)):
    result[index] = prefix

    prefix *= arr[index]

  postfix = 1

  for index in range(len(arr)-1, -1, -1):
    result[index] = postfix * result[index]

    postfix *= arr[index]
  return result

print('product_except_self([1, 2, 3, 4]):', product_except_self([1, 2, 3, 4]))