def integer_to_roman(num: int) -> str:
    val = [
      1000, 900, 500, 400,
      100, 90, 50, 40,
      10, 9, 5, 4,
      1
    ]

    syms = [
      "M", "CM", "D", "CD",
      "C", "XC", "L", "XL",
      "X", "IX", "V", "IV",
      "I"
    ]
    
    res = ""
    for i in range(len(val)):
      # How many times this symbol fits
      count = num // val[i]
      res += syms[i] * count

      # Reduce the number
      num -= val[i] * count
    return res

print('integer_to_roman(3749):', integer_to_roman(3749))