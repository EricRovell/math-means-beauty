# convert the digits representation of a number from base 'b' to base 'c'
def convert_base(number, base, into = None):

  # convert a positive 'number' to it's digit representation in 'base'
  def to_digits(number, base):
    digits = []
    while number > 0:
      digits.insert(0, number % base)
      number //= base
    return digits

  # compute the number given by digits in 'base'
  def from_digits(digits, base):

    if isinstance(digits, int):
      digits = [int(digit) for digit in str(digits)]
    elif isinstance(digits, str):
      digits = [int(digit) for digit in digits]

    # validating number
    if any(digit >= base for digit in digits):
      return None

    number = 0
    for digit in digits:
      number = number * base + digit

    return number

  # number -> to base
  if into == None:

    if isinstance(number, int):
      return to_digits(number, base)

    # digits -> number in base  
    elif isinstance(number, str) or isinstance(number, list):
      return from_digits(number, base)

  elif isinstance(into, int):
    return to_digits(from_digits(number, base), into)
  

print(convert_base(241, 5))