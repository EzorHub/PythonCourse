def cal(a, b):
  if(type(a) == str or type(b) == str):
    result = "that's not available. check it again."
    #int, float을 계산하게 해주고 싶었음 - 유효성 검사를 해주기
  else:
    what_you_input = f"{a}, {b}"
    # 혹시 뭔 숫자 입력했는지 궁금할까봐
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
    #dictionary에 익숙해지기도 하고 한번에 결과값을 보여주면 좋을 것같아서
  return result
  #아직도 리턴위치는 어렵습니다

print(cal(a ="lalalalalala", b=5))
print(cal(a =3, b=5))

#한 30분은 왜 계산이 안되지라고 고민한 것 같다. 수식은 맞는데 대체 왜? 
#생각해보니까 result라는 변수에 리턴값을 담았을뿐, 출력을 안했으니 콘솔엔 아무것도 안찍힐수밖에..!ㅎㅎ
