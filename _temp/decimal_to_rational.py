# returns the rational fraction as a string: 'numerator / denominator'
# from a given decimal fraction
def decimal_to_rational(fraction):
  # we need string as the parameter
  if isinstance(fraction, float):
    fraction = str(fraction)
  
  isPeriodic = True if '(' and ')' in fraction else False
  # is the fraction regular
  unit = 0 if fraction[0] == '.' else fraction[0]
  # the fraction is periodic
  if isPeriodic:
    period = fraction[fraction.index( '(' ) + 1 : fraction.index( ')' )]
    non_period = fraction[fraction.index('.') + 1 : fraction.index( '(' )]
    mantissa = f'{non_period}{period}'
    if non_period != '':
      numerator = int(mantissa) - int(non_period)
    else:
      numerator = int(mantissa)
    denominator = int( '9' * len(period) + '0' * len(non_period) )
  # fraction is non-periodic
  else:
    mantissa = fraction[fraction.index('.') + 1 :]
    numerator = int(mantissa)
    denominator = 10 ** len(mantissa)
  if unit != 0:
    numerator += int(unit) * int(denominator)
  return numerator, denominator
 

# tests
print(decimal_to_rational('.23'))
print(decimal_to_rational('.23(36)'))
print(decimal_to_rational('3.2346'))
print(decimal_to_rational('1.23(786)'))
print(decimal_to_rational(2.02))
print(decimal_to_rational('0.(2)'))