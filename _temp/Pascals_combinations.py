def pascals(rows):

  factorials = {0: 1, 1: 1}
  def factorial(number):
    if number not in factorials:
      result = number * factorial(number - 1)
      factorials[number] = result
      return result
    else:
      return factorials[number]

  def combinations(n, k):
    return int( factorial(n) / factorial(k) / factorial(n - k) )

  triangle = [ [1] for _ in range(rows) ]
  for n in range(1, rows):
    for k in range(1, n + 1):
      triangle[n].append(combinations(n, k))

  return triangle

print(pascals(8))