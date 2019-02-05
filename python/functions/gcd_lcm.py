# returns the greatest common divisor
def gcd(a, b):
  if a < b: return gcd(b, a)
  while b:
    a, b = b, a % b
  return a

# returns the least common multiple
def lcm(a, b):
  return a * b // gcd(a, b)

# evaluates if the numbers are coprime
def iscoprime(a, b):
  return gcd(a, b) == 1