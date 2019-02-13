# sieve of Atkin
def asieve(limit):
  assert limit > 3
  sieve = [False] * (limit + 1)
  sieve[2:4] = (True, True)

  # preliminary work
  x, y = 1, 1
  while x**2 < limit:
    while y**2 < limit:

      n = 4 * x**2 + y**2
      if n <= limit and n % 12 in (1, 5):
        sieve[n] = not sieve[n]

      n = 3 * x**2 + y**2
      if n <= limit and n % 12 == 7:
        sieve[n] = not sieve[n]

      if x > y:
        n = 3 * x**2 - y**2
        if n <= limit and n % 12 == 11:
          sieve[n] = not sieve[n]

      y += 1
    x, y = x + 1, 1
    
  # remove the squares of primes (and their multiples)
  r = 5
  while r**2 < limit:
    if sieve[r]:
      for n in range(r**2, len(sieve), r**2):
        sieve[n] = False
    r += 1
    
  # append everything into a list
  return [value for value, isprime in enumerate(sieve) if isprime]

# tests
print(len(asieve(1000000)))