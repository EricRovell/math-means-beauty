# limit
# index
# list
# isFib
# sum

def fibonacci(limit):
  sequence = [0, 1]
  if limit == 0: return 0
  if limit == 1: return sequence
  if limit < 0: raise IndexError
  
  while True:
    number = sequence[-1] + sequence[-2]
    if number < limit:
      sequence.append(number)
    else:
      break

  return sequence

def zeckendorf_representation(number):
  fib_list = fibonacci(number)
  representation = []

  if number == fib_list[-1]:
    return number

  k = -1
  while True:
    representation.append(fib_list[k])

    if representation
    
print(zeckendorf_representation(100))