def p_plus(a, b):
  print(a+b)

def r_plus(a, b):
  return a + b

p_result = p_plus(3, 13)
r_result = r_plus(3, 13)

print("p_result: ",p_result," r_result:", r_result)
# p_result는 리턴값이 없으므로 None == null 