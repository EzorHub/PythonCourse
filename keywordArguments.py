def say_hello(name,age):
  return f"Hello {name} you are {age} years old"

#f 는 format인데, f를 앞에 붙여주고 {}안에 파라미터 이름 써주면 자동으로 입력받음
# "hello "+name+"you are "+age+" years old" 이거보다 훨씬 간편하네요잉
hello = say_hello("zozo", "00")
#hello = say_hello(name="zozo", age="00") keyword argument는 순서와 상관없이 인자를 키워드로 인식함!
print(hello)