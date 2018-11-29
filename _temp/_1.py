def rational_to_decimal(numerator, denominator, limit = None, get_period = False):
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

print(rational_to_decimal(1, 99))