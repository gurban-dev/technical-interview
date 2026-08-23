def is_anagram(s: str, t: str) -> bool:

    # 1. Check whether both strings have the same length.
    #    If they have different lengths, they cannot be anagrams.

    # 2. Create a dictionary for each string to store the frequency
    #    of every character.

    # 3. Iterate through both strings at the same time.

    # 4. For each character, increment its frequency in the
    #    corresponding dictionary.

    # 5. Compare the two dictionaries.
    #    If they contain the same characters with the same
    #    frequencies, the strings are anagrams.

    # 6. Return True if the dictionaries are equal.
    #    Otherwise, return False.
    
    # First, verify that both strings have the same length.
    # Anagrams must contain the same number of characters.
    if len(s) == len(t):

        dict_s = {}
        dict_t = {}

        # The .get() method returns the value associated with a key,
        # or a default value if the key does not exist.

        # enumerate() gives us both the index and character.
        # We only need the index, so we use _ as a throwaway variable
        # to ignore the character we do not need.
        for i, _ in enumerate(s):

            # Get the character's current count, or 0 if it is not in the dictionary,
            # then increase the count by 1.
            dict_s[s[i]] = dict_s.get(s[i], 0) + 1
            dict_t[t[i]] = dict_t.get(t[i], 0) + 1

        # Two strings are anagrams if their character frequencies match.
        return dict_s == dict_t
    
    else:
        return False

# LeetCode Pattern:
# Hash Map / Frequency Counter

# This pattern can be identified in problems where you need to keep track
# of how many times each value appears. A dictionary is useful because it
# lets you store each value as a key and its count as the corresponding value.

# Time Complexity: O(n), where n is the length of the strings.
# Space Complexity: O(n), for storing character frequencies.

print("is_anagram(\"racecar\", \"carrace\"):", is_anagram("racecar", "carrace"), "\n")

print("is_anagram(\"jar\", \"jam\"):", is_anagram("jar", "jam"), "\n")

print("is_anagram(\"x\", \"x\"):", is_anagram("x", "x"))