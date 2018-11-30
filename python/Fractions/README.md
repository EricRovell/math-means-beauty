# Fractions

Fractions class can construct fraction-objects as tuple *(numerator, denominator)*. After initialization or any arithmetic operation the fraction is simplified.

> (25, 100) -> (1, 4)

Fraction can be initialized using several optional arguments:

- integer: 
  ```
  >>> fraction_from_integer = Fraction(5)
  >>> (5, 1)
  ```

- tuple *(int, int)* :

  ```
  >>> fraction_from_tuple = Fraction(4, 9)
  >>> (4, 9)
  ```

- float

  ```
  >>> fraction_from_float = Fraction(0.05)
  >>> (5, 100)

- string:

  ```
  >>> fraction_from_string = Fraction('2/5')
  >>> (2, 5)
  ```

  ```
  >>> non_periodic_decimal = Fraction('0.01')
  >>> (1, 100)
  ```

  ```
  >>> periodic_decimal = '0.1(23)'
  >>> (61, 485)
  ```

---

# Available methods


