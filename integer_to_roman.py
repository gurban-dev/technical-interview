def integer_to_roman(num: int) -> str:
  # Values (descending) that cover all allowed Roman "tokens",
  # including the subtractive pairs (900, 400, 90, 40, 9, 4).
  val = [
    1000, 900, 500, 400,
    100, 90, 50, 40,
    10, 9, 5, 4,
    1
  ]

  # Corresponding Roman symbols for each value above, same order.
  syms = [
    "M", "CM", "D", "CD",
    "C", "XC", "L", "XL",
    "X", "IX", "V", "IV",
    "I"
  ]
  
  res = ""

  # Iterate over each Roman "token" from largest to smallest.
  for i in range(len(val)):
    # Find out how many times this symbol fits.
    count = num // val[i]

    res += syms[i] * count

    # Reduce the number
    num -= val[i] * count
  return res

print('integer_to_roman(3749):', integer_to_roman(3749))

print('\ninteger_to_roman(58):', integer_to_roman(58))

print('\ninteger_to_roman(1994):', integer_to_roman(1994))

'''
Input:
An integer num such that 1 ≤ num ≤ 3999

Output:
A string representing the Roman numeral form of num.

1. Initialise value-symbol pairs.
   Create two ordered lists that represent the Roman numeral
   system, including the subtractive forms.

   These lists are parallel, meaning:
   1000 corresponds to "M"

   900 corresponds to "CM"

2. Initialise the result string.

3. Iterate over all values (largest to smallest)
   For each index i from 0 to len(val) - 1:
   a. Compute how many times the current Roman value fits:

      count = num // val[i]

   b. Append that symbol to the result string:

      res = res + (syms[i] * count)

   c. Reduce the number:

      num = num - (val[i] * count)

      If num becomes 0, all parts of the number have been
      converted—exit the loop early (optional optimization).

4. Return the result.
'''