# babylonian method: sqrt
def sqrt(number, precision):
  initial_guess = number / 2
  difference = 1

  while difference > precision:
    guess = 0.5 * (initial_guess + number / initial_guess)
    difference = initial_guess - guess
    initial_guess = guess

  guess = str(guess)
  return float( guess[ : guess.index('.') + len(str(precision)) - 1] )

# tests
print(sqrt(1021113, 0.0001))