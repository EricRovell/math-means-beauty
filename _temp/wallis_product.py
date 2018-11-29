def wallis_product(iterations):
  numerator, denominator = 2, 1
  product = [numerator, denominator]

  if iterations <= 1: return 2
  
  i = 2
  while i < iterations:

    if i % 2 == 0:
      denominator += 2
    else:
      numerator += 2
    
    product[0] *= numerator
    product[1] *= denominator
    i += 1
  
  return 2 * product[0] / product[1]

print(wallis_product(10000))