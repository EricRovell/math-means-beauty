def rational_to_decimal(numerator, denominator, get_period = False, limit = None, repetition = True):
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
    
    if repetition:
      previous_index = states.get(divident, None)
      if previous_index != None:
        # fraction -> unit.non_periodic(period)
        period_start = previous_index
        non_periodic = decimal[ :period_start]
        period = decimal[period_start: ]

        if get_period: return f'{period}'
        return f'{non_periodic}({period})'

      states[divident] = len(decimal)
      
    unit = divident // denominator
    decimal += str(unit)
    divident = 10 * (divident - unit * denominator)
    if limit != None: limit -= 1
  
  if divident > 0: return f'{decimal}...'
  if get_period: return None
  return decimal

print(rational_to_decimal(3, 100))