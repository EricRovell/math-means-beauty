# generates the digits from the integer
# works from reverse order!
def digits(number):
  while number:
    yield number % 10
    number //= 10

# returns sum of the digits of the integer
def digitsum(number):
  total = 0
  while number:
    total, number = total + number % 10, number // 10
  return total

print(digitsum(5634))