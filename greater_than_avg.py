# Count Elements Greater Than Previous Average

# Given an array of positive integers, return the number of
# elements that are strictly greater than the average of all
# previous elements. Skip the first element.

# Example

# Input
# responseTimes = [100, 200, 150, 300]

# Output
# 2

# Input: An array/list of positive integers.
# Output: A single integer.

# 1. Create a variable called 'count' that keeps track of how
#    many elements qualify (greater than the average of all
#    previous elements).

# 2. Create a variable called 'previous_sum' that keeps track
#    of the sum of the elements previously visited.

# 3. Start at the second element, because the first must be skipped.

# 4. Calculate the previous average by dividing 'previous_sum' by
#    the number of previous elements.

# 5. If the current element is greater than the previous average,
#    increase 'count' by one.

# 6. Add the current element to 'previous_sum' so it becomes part
#    of the sum of the previous elements for the next iteration.

# 7. Return 'count'.

def countResponseTimeRegressions(responseTimes):
    count = 0

    # range(start (inclusive), stop (exclusive)) expects an integer.
    # The stop value is exclusive, so len(responseTimes) is not included
    # in the range of integers.
    
    # Return early if there are fewer than two integers to compare.
    if len(responseTimes) < 2:
        return count

    previous_sum = responseTimes[0]

    # range(5) generates 0, 1, 2, 3, 4 (5 is left out)
    for index in range(1, len(responseTimes)):

        # 'index' will equal the number of previous elements.
        # When dividing with /, a float is always returned.
        average = previous_sum / index

        if responseTimes[index] > average:
            count += 1

        # Add the current element to 'previous_sum' for the next
        # iteration.

        # The average must include only the elements that came
        # before the current element.

        # Indices:          0    1    2    3
        # responseTimes = [100, 200, 150, 300]

        # Suppose we are currently processing the element 150 at index 2.

        # Before processing 150:
        # previous_sum = 100 + 200 = 300
        # index = 2
        # average = previous_sum / index = 300 / 2 = 150.0

        # Since 150.0 is not greater than 150, 'count' is not increased.

        # However, we must still add 150 to previous_sum because it
        # becomes part of the previous elements when we process 300.

        # If we did not update previous_sum:
        # previous_sum would remain 300.
        # When processing 300, 'average' would incorrectly be 300 / 3 = 100.

        # By updating previous_sum:
        # previous_sum = 300 + 150 = 450
        # When processing 300, average = 450 / 3 = 150.

        # Now 300 > 150, so we correctly increment 'count'.

        # Every processed element must be added to 'previous_sum'
        # regardless of whether it increases 'count'.

        # This ensures that the average includes all elements before the
        # current element, excluding the current element itself.
        
        previous_sum += responseTimes[index]

        # The above augmented addition assignment operator is a
        # concise way to write the following:
        # previous_sum = previous_sum + responseTimes[index]

    return count

# Time Complexity: O(n), because each element is visited at most
#                  once.

# Space Complexity: O(1), since only a fixed number of variables
#                   are used.

if __name__ == '__main__':
    responseTimes_count = int(input().strip())

    responseTimes = []

    for _ in range(responseTimes_count):
        responseTimes_item = int(input().strip())
        responseTimes.append(responseTimes_item)

    result = countResponseTimeRegressions(responseTimes)

    print(result)