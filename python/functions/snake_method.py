# TODO: number validation

def snake_method(number, base, into_base):
  if base == into_base: return number
  if number == 0: return 0

  representation = []
  digits = [int(digit) for digit in str(number)]

  if base < into_base:
    result = digits.pop(0)
    for digit in digits:
      result *= base
      result += digit
    
    return result

  else:
    number = int(number)
    while number > 0:
      if number % into_base != 0:
        representation.insert(0, number % into_base)
        # number -= number % into_base
        number //= into_base
      else:
        representation.insert(0, number % into_base)
        number //= into_base
        
    return representation

def numberToBase(n, b):
  if n == 0:
    return [0]
  digits = []
  while n:
    digits.append(int(n % b))
    n //= b
  return digits[::-1]
  
print(snake_method('563', 10, 8))
    