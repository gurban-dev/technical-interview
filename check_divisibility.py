def check_divisibility(n):

    # 1. Store the original number because n will be reduced
    #    while we extract its digits.

    # 2. Create variables to store the sum and product of the digits.

    # 3. While n is greater than 0:
    #    a. Get the last digit using n % 10.
    #    b. Add the digit to the digit sum.
    #    c. Multiply the digit into the digit product.
    #    d. Remove the last digit using n // 10.

    # 4. Add the digit sum and digit product to get the divisor.

    # 5. Check whether the original number is divisible by the divisor.

    # 6. Return True if it is divisible, otherwise return False.

    # Store the original number because n will be reduced while extracting digits.
    original = n

    # The product starts at 1 because 1 is the multiplicative identity.
    digit_sum = 0
    digit_product = 1

    # Extract and process each digit from right to left.
    while n > 0:
        # Get the last digit of n by using the remainder operator.
        digit = n % 10

        # Add the last digit to the digit sum.
        digit_sum += digit

        # Multiply the last digit into the digit product.
        digit_product *= digit

        # Remove the last digit from n using floor division (//).
        n //= 10

    # Compute the required divisor.
    divisor = digit_sum + digit_product

    # Return True or False depending on whether the original number is
    # divisible by the divisor.
    return original % divisor == 0

# LeetCode Pattern:
# Math / Digit Manipulation

# This pattern can be identified in problems where you need to work
# directly with the individual digits of a number. Operations such as
# % 10 can be used to get the last digit, while // 10 removes it.

# Time Complexity: O(d), because we process each digit in n once,
#                  d represents the number of digits in the integer n.
# Space Complexity: O(1), because we only use a fixed number of variables
#                   regardless of how many digits n has.

print("check_divisibility(99):", check_divisibility(99), "\n")

print("check_divisibility(23):", check_divisibility(23))