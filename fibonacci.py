def fibonacci_list(n):
  if n == 0:
    return []
  elif n == 1:
    return [0]

  # Start with the first two Fibonacci numbers [0, 1].
  fib_numbers = [0, 1]

  # Loop from 2 to n-1 (because the first two numbers are
  # already in the list).

  # In this context, _ is a throwaway placeholder, which is used
  # when a value is not needed.
  for _ in range(2, n):
    # Calculate the next number by adding the last two numbers
    # in the list: fib_numbers[-1] + fib_numbers[-2].
    next_number = fib_numbers[-1] + fib_numbers[-2]

    # Append the sum of the last two numbers to the list.
    fib_numbers.append(next_number)

  # At the end, the list contains the first n Fibonacci numbers.
  return fib_numbers

print('fibonacci_list(0):', fibonacci_list(0))

print('fibonacci_list(1):', fibonacci_list(1))

print('fibonacci_list(5):', fibonacci_list(5))

print('fibonacci_list(10):', fibonacci_list(10))