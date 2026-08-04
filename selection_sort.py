def selection_sort(arr):
  for i in range(len(arr)):
    # Assume the first element of the unsorted portion is the minimum.
    index_of_min = i

    for j in range(i + 1, len(arr)):
      if arr[j] < arr[index_of_min]:
        index_of_min = j

    # Swap the found minimum with the first element of the unsorted portion.
    arr[i], arr[index_of_min] = arr[index_of_min], arr[i]
  return arr

arr = [3, 2, 1]

print(f'selection_sort({arr}): {selection_sort(arr)}')