def esieve(limit):
  # we start sieve from 3, all numbers assumed to be odd
  # [0 -> 3, 1 -> 5, 2 -> 7, ...]
  size = (limit // 2 - 1) if limit % 2 == 0 else (limit // 2)
  sieve = size * [1]

  # index to number: i -> 2i + 3
  # we start to sieve from the prime^2, so:
  #   starting point: index + prime
  #   jump: prime
  yield 2
  for index, isprime in enumerate(sieve):
    if isprime:
      prime = 2 * index + 3
      yield prime
      for multiple in range(index + prime, size, prime):
        sieve[multiple] = 0

print(len(list(esieve(100))))


