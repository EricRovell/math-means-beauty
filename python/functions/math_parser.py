from collections import deque
import re

numeric_value = re.compile(r'\d+(\.\d+)?')

__operators__ = '+-/*^'
__parenthesis__ = '()'
__priority__ = {
  '+': 0,
  '-': 0,
  '*': 1,
  '/': 1,
  '^': 2
}

# check if token it's operator
def is_operator(token):
  return token in __operators__

# check if operation_1 has higher priority than operation_2
def higher_priority(operation_1, operation_2):
  return __priority__[operation_1] >= __priority__[operation_2]

# calculate operation result
def calculate(b, a, operator):
  # number_1 -> a
  # number_2 -> b
  if operator == '+':
    return a + b
  elif operator == '-':
    return a - b
  elif operator == '*':
    return a * b 
  elif operator == '/':
    return a / b 
  elif operator == '^':
    return a ** b
  return 0

# apply operation to the first two items if the output queue
def apply_operation(operation_stack, output_stack):
  output_stack.append( calculate(output_stack.pop(), output_stack.pop(), operation_stack.pop()) )

# return array of parsed tokens in the expression
# expression: String
def parse(expression):
  result = []
  current = ''
  for char in expression:
    if char.isdigit() or char == '.':
      current += char
    else:
      if len(current) > 0:
        result.append(current)
        current = ''
      if char in __operators__ or char in __parenthesis__:
        result.append(char)
      else:
        raise Exception('invalid syntax ' + char)
  
  if len(current) > 0:
    result.append(current)

  return result



# calculate the result of expression
# expression String
# type Type (optional): Number type [int, float]
def evaluate(expression):
  operation_stack = deque()
  output_stack = deque()

  tokens = parse(expression)
  for token in tokens:
    
    if numeric_value.match(token):
      output_stack.append(float(token))
    elif token == '(':
      operation_stack.append(token)
    elif token == ')':
      while len(operation_stack > 0) and operation_stack[-1] != '(':
        apply_operation(operation_stack, output_stack)
      # remove remaining '('
      operation_stack.pop()
    else:
      # is_operator(token)
      while len(operation_stack) > 0 and is_operator(operation_stack[-1]) and higher_priority(operation_stack[-1], token):
        apply_operation(operation_stack, output_stack)
      operation_stack.append(token)

  while len(operation_stack) > 0:
    apply_operation(operation_stack, output_stack)
  operation_stack.append(token)

  return output_stack[-1]


print(evaluate('2+2*2-5^3'))