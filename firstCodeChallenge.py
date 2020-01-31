def cal(a, b):
  if(type(a) == str or type(b) == str):
    result = "that's not available. check it again."
  else:
    what_you_input = f"{a}, {b}"
    plus = a + b
    minus = a - b
    times = a * b
    division = a / b
    negation = -a
    power = a ** b
    reminder = a % b

    result = {
      "what you input": what_you_input,
      "plus":plus,
      "minus":minus,
      "times":times,
      "division":division,
      "negation":negation,
      "power":power,
      "reminder":reminder
    }
  return result

print(cal(a ="lalalalalala", b=5))
print(cal(a =3, b=5))
