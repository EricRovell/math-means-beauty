# returns the square root of the given number up to required number of digits
# integral -> integral part of the number as a list of digits
# fractional -> fractional part of the number as a list of digits
# digits - how many digits after the decimal point
def sqrt(integral, fractional, digits):
  # 12.56 -> [1,2], [5,6]
      
  # digits shall be broken into pairs
  # odd number of digits -> 123.123: 0123.1230
  # 0 in front of integral part;
  # 0 at the end of the fractional part;
  if len(integral) % 2 == 1: integral.insert(0, 0)
  if len(fractional) % 2 == 1: fractional.append(0)
       
  if len(fractional) < 2 * digits:
    fractional.extend( [0] * (2 * digits - len(fractional)) )
            
  # making the pairs of digits: 0123.1430 -> 01 23 . 14 30
  digitcouples = {
    'integral'  : [10 * tens + digit for tens, digit in zip(integral[::2], integral[1::2])],
    'fractional': [10 * tens + digit for tens, digit in zip(fractional[::2], fractional[1::2])]
  }

  result = {
    'integral'  : list(),
    'fractional': list()
  }

  # sqrt integer solution
  def int_sqrt(number):
    initial = number
    seed = (initial + 1) // 2
    while seed < initial:
        initial = seed
        seed = (initial + number // initial) // 2
    return initial

  # p - part of the root found so far
  # r - remainder
  p, r = 0, 0
  for part, pairs in digitcouples.items():
    for num in pairs:
      c = 100 * r + num
      x = (-20 * p + int_sqrt(400 * p ** 2 + 4 * c)) // 2
      y = 20 * p * x + x ** 2
      r = c - y
      p = 10 * p + x
      result[part].append(x)
    
  return result


print(sqrt([1, 6], [0], 10))