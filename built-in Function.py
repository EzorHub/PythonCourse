
# 변수 선언이 없는 이유로 인해 ---변수안에 변수타입을 바꿔서 또 선언해줄 수가 있음, 자바랑 구분되는 특징!
age = "18"
print(age)
print(type(age))
n_age = int(age)
print(n_age)
print(type(n_age))

def say_hello(name="there"):
  print("hello", name)

say_hello()
say_hello("tokki")

def year(n):
  print("this is",n,"year!")

year(2020)