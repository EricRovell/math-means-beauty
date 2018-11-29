def pi_digits(n):
  "Generate n digits of Pi."
  k, a, b, a1, b1 = 2, 4, 1, 12, 4
  while n > 0:
    p, q, k = k * k, 2 * k + 1, k + 1
    a, b, a1, b1 = a1, b1, p * a + q * a1, p * b + q * b1
    d, d1 = a / b, a1 / b1
    while d == d1 and n > 0:
      yield int(d)
      n -= 1
      a, a1 = 10 * (a % b), 10 * (a1 % b1)
      d, d1 = a / b, a1 / b1

print(list(pi_digits(10)))