def insertion_sort(arr):
  for i in range(1, len(arr)):
    current = arr[i]

    j = i - 1

    while j >= 0 and current < arr[j]:
      # 1st for-loop iteration
      # 1st and only while loop iteration:
      # arr[1] = 3

      # 2nd for-loop iteration
      # 1st while loop iteration:
      # arr[2] = 3
      #
      # 2nd while loop iteration:
      # arr[1] = 2
      arr[j + 1] = arr[j]

      # 1st for-loop iteration
      # 1st and only while loop iteration:
      # j = j - 1 -> j = -1

      # 2nd for-loop iteration
      # 1st while loop iteration:
      # j = 0
      #
      # 2nd while loop iteration:
      # j = -1
      j -= 1

    # 1st for-loop iteration:
    # arr[0] = 2

    # 2nd for-loop iteration:
    # arr[0] = 1
    arr[j + 1] = current

    # 1st for-loop iteration:
    # arr becomes [2, 3, 1]

    # 2nd for loop iteration:
    # arr becomes [1, 2, 3]
  return arr

print('insertion_sort([]):', insertion_sort([]))

print('insertion_sort([1]):', insertion_sort([1]))

print('insertion_sort([3, 1]):', insertion_sort([3, 1]))

print('insertion_sort([2, 3, 1]):', insertion_sort([2, 3, 1]))

# print(f'insertion_sort([3, 2, 1]): {insertion_sort([3, 2, 1])}')