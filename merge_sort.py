def merge_sort(arr):
  # Base case
  if len(arr) <= 1:
    return arr

  # mid = 3 // 2 -> 1
  mid = len(arr) // 2

  # left = merge_sort(arr[:1]) -> merge_sort([3])
  # left = [3]

  # left = merge_sort(arr[:1]) -> merge_sort([2])
  # left = [2]
  left = merge_sort(arr[:mid])

  # right = merge_sort(arr[1:]) -> merge_sort([2, 1])
  # right = merge_sort(arr[1:]) -> merge_sort([1])
  # right = [1]
  right = merge_sort(arr[mid:])

  return merge(left, right)

def merge(left, right):
  result = []

  i = j = 0

  # Merge the two sorted lists.
  while i < len(left) and j < len(right):
    if left[i] <= right[j]:
      result.append(left[i])
      i += 1
    else:
      result.append(right[j])
      j += 1

  # Append any remaining elements
  result.extend(left[i:])
  result.extend(right[j:])
  return result

# Corner cases:
# print(f'merge_sort([]): {merge_sort([])}')

# print(f'merge_sort([3]): {merge_sort([3])}')

# print(f'merge_sort([3, 2]): {merge_sort([3, 2])}')

# print(f'merge_sort([3, 3]): {merge_sort([3, 3])}')

print(f'merge_sort([3, 2, 1]): {merge_sort([3, 2, 1])}')

'''
Call stack
merge_sort([3, 2, 1])
│
├─ merge_sort([3])  → returns [3]
│
└─ merge_sort([2, 1])
   │
   ├─ merge_sort([2]) → returns [2]
   │
   └─ merge_sort([1]) → returns [1]
   │
   └─ merge([2], [1]) → returns [1, 2]
│
└─ merge([3], [1, 2]) → returns [1, 2, 3]
'''