import turtle
from types import SimpleNamespace

system = SimpleNamespace(
           axiom = 'X',
           rules = {'F': 'FF', 'X': 'F+[[X]-X]-F[-FX]+X'},
           angle = 25
)

t = turtle.Turtle()
screen = turtle.Screen()

stack = []

# axiom = 'X'
# rules = {'F': 'FF', 'X': 'F+[[X]-X]-F[-FX]+X'}
# angle = 25

t.hideturtle()
t.speed(0)
t.up()
t.goto(0, -350)
t.down()
t.left(90)

t.pencolor('white')
screen.bgcolor('#333333')

def generator(iterations):
  sentence = system.axiom
  for _ in range(iterations):
    next_sentence = '' 
    for char in sentence:
      if char in system.rules:
        next_sentence += system.rules[char]
      else:
        next_sentence += char
    sentence = next_sentence
  return sentence

def interpretator(sentence):
  for char in sentence:
    if char == 'F': 
      t.forward(5)
    elif char == '+': 
      t.left(system.angle)
    elif char == '-': 
      t.right(system.angle)
    elif char == '[':
      stack.append((t.heading(), t.position()))
    elif char == ']':
      direction, position = stack.pop()
      t.up()
      t.goto(position)
      t.setheading(direction)
      t.down()
    else:
      continue

sentence = generator(6)
interpretator(sentence)

turtle.exitonclick()