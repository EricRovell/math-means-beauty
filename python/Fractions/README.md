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

## Setters:

```
>>> fraction = Fraction(1, 5)

>>> fraction.set_fraction(3, 7)  ->  (3, 7)
>>> fraction.set_numerator(2)    ->  (2, 5)
>>> fraction.set_denominator(7)  ->  (1, 7)
>>> fraction.set_reciprocal()    ->  (5, 1)
```

## Getters

```
>>> fraction = Fraction(2, 5)

>>> fraction.get_fraction()      ->  (2, 5)
>>> fraction.get_numerator()     ->  2
>>> fraction.get_denominator()   ->  5
>>> fraction.get_reciprocal()    ->  (5, 2)
>>> fraction.get_decimal()       ->  0.4

>>> fraction.is_proper()         -> True
>>> fraction.is_improper()       -> False
```

  *get_decimal()* method is able to return even periodic fractions. 
To get the period use *get_period()* method; returns 0 is period is absent.
```
>>> fraction = Fraction(13, 99)

>>> fraction.get_decimal()              -> '0.(13)'
>>> fraction.get_period()               -> 13

>>> fraction_another = Fraction(2, 5)
>>> fraction_another.get_period()       -> 0
```

## Arithmetic operations
All arithmetic operations change the state of the fraction.


```
a = Fraction(1, 7)
b = Fraction(2, 3)

a.add(b)        ->  (17, 21)
a.subtract(b)   ->  (-11, 21)
a.multiply(b)   ->  (2, 21)
a.divide(b)     ->  (3, 14)

# static methods: 
  Fraction._add(a, b)
  Fraction._subract(a, b)
  Fraction._multiply(a, b)
  Fraction._divide(a, b)
```

