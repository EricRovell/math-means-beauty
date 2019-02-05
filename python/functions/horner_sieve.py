def horner_sieve(*coefficients):

  def quadratic(*coefficients):
    a, b, c = coefficients

    if a == 0: return None
    if b == 0:
      return None if -c / a < 0 else [(-c / a) ** 0.5, -(-c / a) ** 0.5]
    if c == 0:
      return [0, -b / a]
    
    D = b * b - 4 * a * c
    if D > 0:
      return [(-b + D ** 0.5) / (2 * a), (-b - D ** 0.5) / (2 * a)]
    elif D == 0:
      return [-b / 2 * a]
    elif D < 0:
      return None
    
  if len(coefficients) == 3:
    return quadratic(*coefficients)

  free_term = coefficients[-1]

  # possible integer solutions
  divisors = {1, -1, free_term, -free_term}
  for divisor in range(2, free_term // 2 + 1):
    if free_term % divisor == 0:
      divisors.update({divisor, -divisor, free_term // divisor, -free_term // divisor})

  #
  for divisor in divisors:
    product = coefficients[0]
    next_sieve = [product]      

    for index in range(len(coefficients) - 1):
      product = divisor * product + coefficients[index + 1]
      next_sieve.append(product)

    if next_sieve[-1] == 0: return next_sieve[:-1] 

  return None

print(horner_sieve(1, 2, -13, -14, 24))
# print(horner_sieve(1, 0, -25))
