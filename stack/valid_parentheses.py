# The key observation:
# A closing bracket must match the most recently opened
# unmatched bracket.

# That is a Last In, First Out (LIFO) relationship, so a
# stack is the natural data structure.

# We must remember:
# Which opening brackets are currently unmatched, and which
# one was opened most recently.

# Example:
# ([{}])

# Suppose we are at the first character, "(", and we haven't seen
# its closing ")" yet, so we have to remember it:
# stack = ["("]

# On the next character, we have to remember "[":
# stack = ["(", "["]

# Next iteration:
# stack = ["(", "[", "{"]

# The most recent bracket was "{". We can remove it since we now
# have reached a closing bracket.

# The last bracket inserted into the stack, "{", is the first
# bracket that will be removed.

# Now that the "{" has been removed, we now have "[".

# The stack gives us the LIFO behavior we need:
# push -> remember an opening bracket
# pop  -> remove the most recently remembered opening bracket
# top  -> inspect the most recently remembered opening bracket

# In Python, stack[-1] gives us the top of the stack.

# Pseudocode

# Naive Approach:
# FUNCTION isValid(s):

#     WHILE s contains "()", "[]", or "{}":
#         Remove one matching pair from s

#     IF s is empty:
#         RETURN true
#     ELSE:
#         RETURN false

# Example:
# "((()))" -> "(())" -> "()" -> ""

# We remove a matching pair three times.

# Each time, we may need to scan the remaining string to find
# a matching pair.

# In this case, n is the number of brackets.

# Input size: n characters

# Each scan looks through the characters in the string
# to find a matching pair.

# Scan 1 -> check up to n characters
# Scan 2 -> check up to n characters
# Scan 3 -> check up to n characters
# ...
# Scan n -> check up to n characters

# In the worst case:
# n scans × n characters checked per scan -> n × n -> n^2

# Therefore:
# Time complexity = O(n^2)

# If we reach a point where there are no matching adjacent pairs
# but the string isn't empty, then it's invalid.

# Time complexity is about how the amount of work grows as the input
# n, gets larger.

# Time complexity: O(n^2) since this approach does O(n) work up to
# O(n) times.
# Space complexity: O(n) because modifying the string can require
# creating new strings whose size is proportional to n.

# "([{}])"

# Optimal approach:
# FUNCTION isValid(s):
#     stack = empty stack

#     close_to_open = {
#         ")" -> "(",
#         "]" -> "[",
#         "}" -> "{"
#     }

#     FOR each character c in s:
#         IF c is a closing bracket:
#             IF stack is empty:
#                 RETURN false

#             IF stack.top != close_to_open[c]:
#                 RETURN false

#             stack.pop()
#         ELSE:
#             stack.push(c)
#
#     RETURN stack is empty

# The last line means:
# Empty stack -> all brackets were matched -> true.
# Non-empty stack -> unmatched opening brackets remain -> false.

# In Python, this is written as:
# return not stack

# close_to_open is a mapping from each closing bracket to the
# opening bracket that it should match.

# If character is ")", close_to_open[character] gives us "(".
# We then check whether "(" is at the top of the stack.

# Example:
# "[}"

# stack = ["["]
# character = "}"

# close_to_open["}"] -> "{"
# stack[-1] -> "["

# "[" != "{"

# Therefore, return False.

# If c is a closing bracket this asks:
# Is the current character something like ), ], or }?

# c = "[" -> No
# c = "]" -> Yes

# This is important because opening brackets get pushed to
# the stack, while closing brackets need to be matched against
# the stack.

# stack[-1] -> what unmatched opening bracket is currently
# at the top of the stack?

# close_to_open[character] -> what opening bracket should this
# closing bracket match?

# If they are equal, we have a valid match.

# For example:
# stack = ["(", "[", "{"]
# character = "}"

# stack[-1] -> "{"
# close_to_open[character] -> close_to_open["}"] -> "{"

# "{" == "{" -> valid match

# We then use stack.pop() to remove "{" from the stack.

# close_to_open = {
#     ")" -> "(",
#     "]" -> "[",
#     "}" -> "{"
# }

# Time Complexity:
# We go through each character in the string once.
# n characters -> O(n) time.

# Space Complexity:
# The stack can store up to n opening brackets.
# n brackets stored -> O(n) space.

def is_valid(s: str) -> bool:
    stack = []

    close_to_open = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    for character in s:

        if character in close_to_open:

            # If c is a closing bracket this asks:
            # Is the current character something like ), ], or }?

            # c = "[" -> No
            # c = "]" -> Yes

            # Suppose:
            # "(}"

            # stack = ["("]

            # stack[-1] -> "("
            # character -> "}"
            # close_to_open["}"] -> "{"

            # Therefore:
            # stack[-1] == close_to_open[character]
            # "(" == "{"
            # False

            # So we return False.

            # "stack" checks that the stack is not empty.

            # We cannot inspect stack[-1] if the stack is empty.
            # An empty stack also means there is no opening bracket
            # available to match the closing bracket.
            if stack and stack[-1] == close_to_open[character]:
                stack.pop()
            else:
                return False
        else:
            stack.append(character)

    # If we reach this point, we never encountered an invalid
    # closing bracket.

    # The only remaining question is whether there are any
    # unmatched opening brackets.

    # Empty stack -> all brackets were matched -> True.
    # Non-empty stack -> some opening brackets remain -> False.

    # Return True if the stack is empty. Otherwise, return False.
    return not stack