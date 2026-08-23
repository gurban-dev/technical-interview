def two_sum(nums: list[int], target: int) -> list[int]:
    # Empty dictionary. Note that sometimes dictionaries are called
    # hash maps.
    prev_map = {}

    # Iterate through the list/array once while keeping track of each
    # element's index.
    for index, element in enumerate(nums):
        # A complement is the amount needed to reach a desired total.

        # Calculate the complement needed to reach the target.
        # If the complement was seen earlier, a pair has been found.
        diff = target - element

        # Look up the complement in the hash map.
        # This is the key hash map lookup step of the pattern in this
        # problem.
        if diff in prev_map:
            return [prev_map[diff], index]

        # Store the current element and its index so future elements
        # can look it up as their complement.
        prev_map[element] = index

# Time complexity: O(n) because the program iterates through the list once.
# Space complexity: O(n) because the hash map may store up to n elements.

nums = [3, 4, 5, 6]
target = 7

print("two_sum(nums, target):", two_sum(nums, target), "\n")

nums = [4, 5, 6]
target = 10

print("two_sum(nums, target):", two_sum(nums, target), "\n")

nums = [5, 5]
target = 10

print("two_sum(nums, target):", two_sum(nums, target))
