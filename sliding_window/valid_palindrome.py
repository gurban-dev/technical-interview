# Check whether a character is an uppercase letter, lowercase
# letter, or digit.
def alpha_num(c):
    # Checks whether the character's ASCII value falls between:
    # A (65) and Z (90), meaning it is an uppercase letter.

    # a (97) and z (122), meaning it is a lowercase letter.

    # 0 (48) and 9 (57), meaning it is a digit.

    # The or operator means that the function returns True if
    # any one of these three conditions is satisfied.
    return (ord('A') <= ord(c) <= ord('Z') or
            ord('a') <= ord(c) <= ord('z') or
            ord('0') <= ord(c) <= ord('9'))


def is_palindrome(s):
    l, r = 0, len(s) - 1

    # Continue comparing characters until the pointers meet.
    while l < r:

        # Skip non-alphanumeric characters from the left.
        while l < r and not alpha_num(s[l]):
            l += 1

        # Skip non-alphanumeric characters from the right.
        while r > l and not alpha_num(s[r]):
            r -= 1

        # Compare both characters without considering case.
        if s[l].lower() != s[r].lower():
            return False

        # Move both pointers one position toward the center.
        l, r = l + 1, r - 1

    return True

s = "A man, a plan, a canal: Panama"

print(is_palindrome(s))

# Example:
# s = "A man, a plan, a canal: Panama"

# Initial positions:
# l = 0 -> 'A'
# r = 29 -> 'a'

# Step 1: Compare 'A' and 'a'.
#         They match after converting both to lowercase.
#         Move l right and r left.

# Step 2: Compare ' ' and 'm'.
#         The left pointer skips the space.
#         Compare 'm' and 'm'. They match.

# Step 3: Compare 'a' and 'a'. They match.

# Step 4: The left pointer skips the comma and space.
#         Compare 'n' and 'n'. They match.

# Step 5: Continue skipping punctuation and spaces
#         while comparing matching characters.

# Eventually, the pointers meet in the middle.

# Result: True