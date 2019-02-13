# sieve of eratosthenes
def esieve(limit):
  # 0 and 1 -> False + all other numbers
  numbers = [0] * 2 + [1] * (limit - 2)
  # index -> holds the number value
  for number, isprime in enumerate(numbers):
    if isprime:
      yield number
      if number ** 2 > limit: continue
      for multiple in range(number * number, limit, number):
        numbers[multiple] = False

print(len(list(esieve(10000000))))