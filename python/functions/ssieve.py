# sieve of Sundaram
# remove all integers of the form: i + j + 2ij, where:
#   i, j -> Natural numbers,
#   1 <= i <= j,
#   i + j + 2ij <= limit of sieving
# the remaining numbers are doubled and incremented by 1,
# giving the list of odd prime numbers (excluding 2) below 2n + 2 (limit)
def ssieve(limit):
  # sieving indexes function
  index = lambda i, j: i + j + 2 * i * j
  limit = limit // 2 - 1
  sieve = [0] + [1] * limit
  i, j = 1, 1
  while index(i, j) <= limit:
    while index(i, j) <= limit and i <= j:
      sieve[index(i, j)] = 0
      i += 1
    i, j = 1, j + 1

  yield 2
  # index -> number itself
  # value -> is it prime? (0 / 1)
  for number, isprime in enumerate(sieve):
    if isprime:
      yield number * 2 + 1

# tests
print(len(list(ssieve(1000000))))