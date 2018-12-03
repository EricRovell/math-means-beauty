# returns the greatest common divisor
def gcd(*numbers):
  # Euclid's algorithm
  def _gcd_(a, b):
    while b:
      a, b = b, a % b
    return a

  # gcd(a, b, c) = gcd( gcd(a, b), c )
  result = numbers[0]
  for number in numbers[1:]:
    result = _gcd_(result, number)
  return result


# returns the largest common multiple
def lcm(*numbers):
  result = numbers[0]
  for number in numbers[1:]:
    result = result * number // gcd(result, number)
  return result