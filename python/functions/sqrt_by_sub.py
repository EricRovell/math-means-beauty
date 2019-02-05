# sqrt by subtraction method
# http://www.afjarvis.staff.shef.ac.uk/maths/jarvisspec02.pdf
def sqrt(number, precision):
  limit = 10 ** (precision + 1)
  a, b = 5 * number, 5
  while b < limit:
    if a >= b:
      a, b = a - b, b + 10
    else:
      a, b = a * 100, (b - 5) * 10 + 5
  return b