class Fraction(object):

  # constructor
  def __init__(self, numerator, denominator = None):

    # from integer
    if isinstance(numerator, int) and denominator == None:
      self.numerator = numerator
      self.denominator = 1

    # from string
    if isinstance(numerator, str) and denominator == None:
      fraction = numerator
      # integer-part
      unit = 0 if fraction[0] == '.' else int(fraction[0])

      # from 'numerator/denominator' string
      if '/' in fraction:
        self.numerator = int( numerator[ : numerator.index('/')] )
        self.denominator = int( numerator[numerator.index('/') + 1 : ] )

      # from '0.02(25)' periodic decimal
      elif '(' and ')' in fraction:
      # the fraction is periodic
        period = fraction[fraction.index( '(' ) + 1 : fraction.index( ')' )]
        non_period = fraction[fraction.index('.') + 1 : fraction.index( '(' )]
        mantissa = f'{non_period}{period}'
        if non_period != '':
          self.numerator = int(mantissa) - int(non_period)
        else:
          self.numerator = int(mantissa)
        self.denominator = int( '9' * len(period) + '0' * len(non_period) )
        if unit != 0:
          self.numerator += unit * self.denominator

      # from non-periodic decimal
      else:
        mantissa = fraction[fraction.index('.') + 1 :]
        numerator = int(mantissa)
        denominator = 10 ** len(mantissa)
        if unit != 0:
          numerator += unit * int(denominator)
        self.numerator = numerator
        self.denominator = denominator

    # from tuple -> (int, int)    
    elif isinstance(numerator, int) and isinstance(denominator, int):
      self.numerator = numerator
      self.denominator = denominator if denominator != None else 1

    # from float -> rational
    elif isinstance(numerator, float) and denominator == None:
      fraction = str(numerator) # temp
      # strings
      unit = fraction[ : fraction.index('.')]
      fraction = fraction[fraction.index('.') + 1 : ]
      # building : unit * 10^(number of digits in numerator) + numerator itself
      self.numerator = int(unit) * (10 ** len(fraction)) + int(fraction)
      self.denominator = int( 10 ** len(fraction) )

    # ! zero division check
    if self.denominator == 0: raise ZeroDivisionError()
    # simplify the fraction
    self.simplify()
  

  # returns the Greatest-Common-Divisor for "a" and "b"
  @staticmethod
  def gcd(a, b):
    if b > a: return Fraction.gcd(b, a)
    if a % b == 0: return b
    return Fraction.gcd(b, a % b)

  @staticmethod
  # returns the Least-Common-Multiple
  def lcm(a, b):
    return a * b // Fraction.gcd(a, b)

  # fraction setter
  def set_fraction(self, fraction):
    self.numerator, self.denominator = fraction[0], fraction[1]

  # numerator setter
  def set_numerator(self, numerator):
    self.numerator = numerator

  # denominator setter
  def set_denominator(self, denominator):
    self.denominator = denominator

  # sets fraction to it's reciprocal
  def set_reciprocal(self):
    self.numerator, self.denominator = self.denominator, self.numerator

  # returns fraction
  def get_fraction(self):
    return self.numerator, self.denominator

  # returns the reciprocal
  def get_reciprocal(self):
    return self.denominator, self.numerator

  # returns numerator's value
  def get_numerator(self):
      return self.numerator

  # returns denominator's value
  def get_denominator(self):
    return self.denominator

  # constructs and returns the decimal form as float
  def get_decimal(self, limit = None, get_period = False):
    unit = self.numerator // self.denominator
    # long-division
    divident = 10 * (self.numerator - unit * self.denominator)
    # constructing decimal
    decimal = f'{unit}.'
    
    # long division
    # intermediate divident : index of the string
    # first state index begins from 2 (after zero and dot)
    # same divident means repetition  
    # from the last index that divident was encountered at
    states = {}
    while divident > 0 and (limit == None or limit > 0):

      previous_index = states.get(divident, None)
      if previous_index != None:
        # fraction -> unit.non_periodic(period)
        period_start = previous_index
        non_periodic = decimal[ : period_start]
        period = decimal[period_start : ]

        if get_period: return f'{period}'
        return f'{non_periodic}({period})'

      states[divident] = len(decimal)
        
      unit = divident // self.denominator
      decimal += str(unit)
      divident = 10 * (divident - unit * self.denominator)
      if limit != None: limit -= 1
    
    if divident > 0: return f'{decimal}...'
    # no period -> 0
    if get_period: return 0

    return float(decimal)
  
  # returns a period of the fraction
  # returns 0 if period is absent
  def get_period(self):
    return self.get_decimal(get_period = True)


  # is the fraction proper / improper?
  def is_proper(self):
    return True if self.numerator < self.denominator else False
  def is_improper(self):
    return True if self.numerator > self.denominator else True

  # is the given fraction equal to another?
  def is_equal(self, fraction):
    if self.numerator == fraction.numerator:
      if self.denominator == fraction.denominator:
        return True
      else:
        return False

  # simplifies the fraction
  def simplify(self):
    gcd = Fraction.gcd(self.numerator, self.denominator)
    self.numerator //= gcd
    self.denominator //= gcd

  @staticmethod
  # simplifies the fraction
  def _simplify(fraction):
    numerator, denominator = fraction
    gcd = Fraction.gcd(numerator, denominator)
    return (numerator // gcd, denominator // gcd)

  # returns the sum of the given fraction and another
  def add(self, fraction):
    common = Fraction.lcm(self.denominator, fraction.denominator)
    self.numerator *= common // self.denominator
    self.numerator += fraction.numerator * common // fraction.denominator
    self.denominator = common
    self.simplify()

  # returns the difference of the given fraction and another
  def subtract(self, fraction):
    common = Fraction.lcm(self.denominator, fraction.denominator)
    self.numerator *= common // self.denominator
    self.numerator -= fraction.numerator * common // fraction.denominator
    self.simplify()

  # returns the product of the given fraction and another
  def multiply(self, fraction):
    self.numerator *= fraction.numerator
    self.denominator *= fraction.denominator
    self.simplify()

  # returns the division result of the given fraction and another
  def divide(self, fraction):
    self.numerator *= fraction.denominator
    self.denominator *= fraction.numerator
    self.simplify()

  @staticmethod
  def _compile(fraction):

    if isinstance(fraction, tuple):
      if all(isinstance(number, int) for number in fraction):
        numerator, denominator = fraction[0], fraction[1]

    elif isinstance(fraction, str):
      # integer-part
      unit = 0 if fraction[0] == '.' else int(fraction[0])

      if '/' in fraction:
        numerator = int( fraction[ : fraction.index('/')] )
        denominator = int( fraction[fraction.index('/') + 1 : ] )

      elif '(' and ')' in fraction:
      # the fraction is periodic
        period = fraction[fraction.index( '(' ) + 1 : fraction.index( ')' )]
        non_period = fraction[fraction.index('.') + 1 : fraction.index( '(' )]
        mantissa = f'{non_period}{period}'
        if non_period != '':
          numerator = int(mantissa) - int(non_period)
        else:
          numerator = int(mantissa)
        denominator = int( '9' * len(period) + '0' * len(non_period) )
        if unit != 0:
          numerator += unit * denominator

      # fraction is non-periodic
      else:
        mantissa = fraction[fraction.index('.') + 1 :]
        numerator = int(mantissa)
        denominator = 10 ** len(mantissa)
        if unit != 0:
          numerator += unit * int(denominator)
        numerator = numerator
        denominator = denominator
    
    elif isinstance(fraction, float):
      fraction = str(fraction) # temp
      # strings
      unit = fraction[ : fraction.index('.')]
      fraction = fraction[fraction.index('.') + 1 : ]
      # building : unit * 10^(number of digits in numerator) + numerator itself
      numerator = int(unit) * (10 ** len(fraction)) + int(fraction)
      denominator = int( 10 ** len(fraction) )

    if denominator == 0: raise ZeroDivisionError()
    return numerator, denominator

  @staticmethod
  def _add(fraction_1st, fraction_2nd):
    numerator_1st, denominator_1st = Fraction._compile(fraction_1st)
    numerator_2nd, denominator_2nd = Fraction._compile(fraction_2nd)
    # common denominator
    common = Fraction.lcm(denominator_1st, denominator_2nd)
    #
    numerator = numerator_1st * (common // denominator_1st)
    numerator += numerator_2nd * (common // denominator_2nd)
    return Fraction._simplify((numerator, common))

  @staticmethod
  def _subtract(fraction_1st, fraction_2nd):
    numerator_1st, denominator_1st = Fraction._compile(fraction_1st)
    numerator_2nd, denominator_2nd = Fraction._compile(fraction_2nd)
    # common denominator
    common = Fraction.lcm(denominator_1st, denominator_2nd)
    #
    numerator = numerator_1st * (common // denominator_1st)
    numerator -= numerator_2nd * (common // denominator_2nd)
    return Fraction._simplify((numerator, common))

  @staticmethod
  def _multiply(fraction_1st, fraction_2nd):
    numerator_1st, denominator_1st = Fraction._compile(fraction_1st)
    numerator_2nd, denominator_2nd = Fraction._compile(fraction_2nd)
    return Fraction._simplify((numerator_1st * numerator_2nd, denominator_1st * denominator_2nd))

  @staticmethod
  def _divide(fraction_1st, fraction_2nd):
    numerator_1st, denominator_1st = Fraction._compile(fraction_1st)
    numerator_2nd, denominator_2nd = Fraction._compile(fraction_2nd)
    return Fraction._simplify((numerator_1st * denominator_2nd, denominator_1st * numerator_2nd))
  
  @staticmethod
  def _to_decimal(numerator, denominator, limit = None, get_period = False):
    unit = numerator // denominator
    # long-division
    divident = 10 * (numerator - unit * denominator)
    # constructing decimal
    decimal = f'{unit}.'
      
    # long division
    # intermediate divident : index of the string
    # first state index begins from 2 (after zero and dot)
    # same divident means repetition  
    # from the last index that divident was encountered at
    states = {}
    while divident > 0 and (limit == None or limit > 0):

      previous_index = states.get(divident, None)
      if previous_index != None:
        # fraction -> unit.non_periodic(period)
        period_start = previous_index
        non_periodic = decimal[ : period_start]
        period = decimal[period_start : ]

        if get_period: return f'{period}'
        return f'{non_periodic}({period})'

      states[divident] = len(decimal)
        
      unit = divident // denominator
      decimal += str(unit)
      divident = 10 * (divident - unit * denominator)
      if limit != None: limit -= 1
    
    if divident > 0: return f'{decimal}...'
    # no period -> 0
    if get_period: return 0

    return float(decimal)

  @staticmethod
  def _get_period(numerator, denominator):
    return Fraction._to_decimal(numerator, denominator, get_period = True)


p = Fraction('0.01')
print(p.get_fraction())