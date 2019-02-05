"""
Zeckendorf's theorem states that every positive integer can be represented
uniquely as the sum of one or more distinct Fibonacci numbers in such a way
that the sum does not include any two consecutive Fibonacci numbers.

More precisely, if N is any positive integer, there exist positive integers
c(i) ≥ 2, with c(i) + 1 > c(i) + 1, such that:

N = sum( F(n) )

where F(n) is the n-th Fibonacci number.
Such a sum is called the Zeckendorf representation of N.
The Fibonacci coding of N can be derived from its Zeckendorf representation.

For example, the Zeckendorf representation of 100 is:
100 = 89 + 8 + 3.

There are other ways of representing 100 as the sum of Fibonacci numbers – for example:
100 = 89 + 8 + 2 + 1
100 = 55 + 34 + 8 + 3
but these are not Zeckendorf representations because 1 and 2 are
consecutive Fibonacci numbers, as are 34 and 55.
"""
# fibonacci generator
def fibonacci(index):
  a, b = 0, 1
  for _ in range(index):
    yield a
    a, b = b, a + b

# greedy algorithm
def zeckendorf_representation(number):
  representation = []

  def closest_fibonacci(number):
    if number == 0: return 0
    if number == 1: return 1
    a, b = 0, 1
    while b <= number:
      a, b = b, a + b
    return a

  while number > 0:
    closest = closest_fibonacci(number)
    representation.append(closest)
    number -= closest
  
  return representation

print(zeckendorf_representation(100))