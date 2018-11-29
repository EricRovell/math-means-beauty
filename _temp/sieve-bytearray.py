def sieve(limit):
  # 0 and 1 -> False + all other numbers
  primes = bytearray(b'\x00\x00') + bytearray(b'\01') * (limit - 2)

  # index -> holds the number value
  for number, is_prime in enumerate(primes):
    if is_prime:
      yield number
      
      multiples = b'\0' * len(primes[number * number : limit : number])
      primes[number * number : limit : number] = multiples

print(list(sieve(50)))