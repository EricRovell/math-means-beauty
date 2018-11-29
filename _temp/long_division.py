def decimals(numerator, denominator):    
  while denominator:      
    yield denominator // numerator
    denominator = denominator % numerator * 10

print(list(decimals(3, 2)))