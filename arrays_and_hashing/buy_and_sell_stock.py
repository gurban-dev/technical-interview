# This is an example of the sliding window pattern which
# typically involves the use of two pointers.

def maxProfit(prices: list[int]) -> int:
  left_ptr, right_ptr = 0, 1

  max_profit = 0

  while right_ptr < len(prices):
    if prices[left_ptr] < prices[right_ptr]:
      profit = prices[right_ptr] - prices[left_ptr]

      max_profit = max(profit, max_profit)
    else:
      left_ptr = right_ptr

    right_ptr += 1

  return max_profit