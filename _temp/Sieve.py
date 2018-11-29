# sieve of eratosthenes
def sieve(limit):
  # 0 and 1 -> False + all other numbers
  primes = [False] * 2 + [True] * (limit - 2)

  # index -> holds the number value
  for number, is_prime in enumerate(primes):
    if is_prime:
      yield number

      for multiple in range(number * number, limit, number):
        primes[multiple] = False


print(list(sieve(1000000)))