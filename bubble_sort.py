'''
Original list:
2 4 7 9 1

1st pass: 2 4 7 1 9
# of comparisons: n - 1

2nd pass: 2 4 1 7 9
# of comparisons: n - 2

3rd pass: 2 1 4 7 9
# of comparisons: n - 3

4th pass: 1 2 4 7 9
# of comparisons: n - 4

Worst-case time complexity: O(n^2)

Each pass has fewer comparisons than the previous one.
'''

def swap(arr, j):
  temp = arr[j]

  arr[j] = arr[j + 1]

  arr[j + 1] = temp

def bubble_sort(arr):
  list_length = len(arr)

  # Traverse through all array elements
  for i in range(list_length):
    list_already_sorted = True

    # Last i elements are already in place
    # Subtract i because each iteration requires
    # one less comparison than the previous.
    for j in range(0, list_length - i - 1):
      # Traverse the array from 0 to list_length - i - 1
      # Swap if the element found is greater than the next element
      if arr[j] > arr[j + 1]:    
        swap(arr, j)

        list_already_sorted = False
    
    if list_already_sorted:
      return arr
      
  return arr

arr = [3, 2, 1]

# arr = []

# arr = [3]

# arr = [3, 3]

# arr = [1, 2, 3]

print(f'bubble_sort({arr}): {bubble_sort(arr)}')