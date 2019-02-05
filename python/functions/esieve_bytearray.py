# sieve of Eratosthenes: bytearray ver.
def esieve(limit):
  # 0 and 1 -> False + all other numbers
  primes = bytearray(b'\x00\x00') + bytearray(b'\01') * (limit - 2)
  # index -> holds the number value
  for number, isprime in enumerate(primes):
    if isprime:
      yield number
      multiples = b'\0' * len(primes[number * number : limit : number])
      primes[number * number : limit : number] = multiples

print(list(esieve(1000000)))