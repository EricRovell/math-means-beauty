# returns the continued expansion of the number's square root
# does not work for perfect squares -> raises ValueError
# https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Continued_fraction_expansion
def expansion(number):
  # sqrt integer solution
  def isqrt(number):
    initial = number
    seed = (initial + 1) // 2
    while seed < initial:
      initial = seed
      seed = (initial + number // initial) // 2
    return initial
  # validation
  if number == isqrt(number) ** 2:
    raise ValueError('The square root of the number should be irrational.')
  
  # m, d, a - in alogorithm description
  complement = 0
  denominator = 1
  addendum = isqrt(number)

  sequence = [addendum]
  while addendum != sequence[0] * 2:
    complement = denominator * addendum - complement
    denominator = (number - complement ** 2) // denominator
    addendum = (sequence[0] + complement) // denominator
    sequence.append(addendum)

  return sequence

# returns the desired rational approximation of sqrt(number)
def approximation(number, order, expansion):
  seed, *period = expansion(number)

  # returns a periodic list of desired length 
  def cycle(iterable, order):
    numbers = [seed]
    while True:
      for addendum in period:
        if len(numbers) >= order:
          return numbers[::-1]
        numbers.append(addendum)

  seed, *addenda = cycle(period, order)
  numerator, denominator = 1, seed 
  for addendum in addenda:
    numerator += addendum * denominator
    denominator = denominator
    # get the reciprocal
    numerator, denominator = denominator, numerator

  # to get the final answer we should get the reciprocal
  return denominator, numerator

# tests
print(approximation(20, 5, expansion))