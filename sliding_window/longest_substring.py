def length_of_longest_substring(s):
    char_set = set()
    l = 0
    res = 0

    for r in range(len(s)):
        while s[r] in char_set:
            char_set.remove(s[l])

            l += 1

        char_set.add(s[r])
        res = max(res, r - l + 1)

    return res

s = "abcdebc"

print(length_of_longest_substring(s))

# A while loop repeatedly removes characters from the left
# until the duplicate disappears from the current window.

# Example: s = "abcdebc"

# When r = 5, we encounter the second 'b':

# Current window:  a b c d e b
#                  0 1 2 3 4 5

# char_set = {'a', 'b', 'c', 'd', 'e'}

# First iteration of while:
# Remove 'a' at index 0.
# l = 1
# 'b' is still in char_set.

# Second iteration of while:
# Remove 'b' at index 1.
# l = 2
# 'b' is no longer in char_set.

# Now we can add the new 'b' at index 5.

# New window: c d e b
# char_set = {'c', 'd', 'e', 'b'}

# Why not use if?
# An if statement executes its body only once.
# It would remove 'a' but leave the previous 'b' in the set.
# The duplicate would therefore remain.

# The while loop is preferable because it keeps removing
# characters until the window contains only unique characters.