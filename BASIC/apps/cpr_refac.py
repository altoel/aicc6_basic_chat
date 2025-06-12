def get_compund_rate(message):
  while True:
    value = input(message)

    try:
      value = float(value)
    except ValueError: # 숫자형 문자가 아닌 경우
      print(f"{value}은 숫자가 아닙니다. 숫자를 입력해 주세요.")
      continue # 

    if value <= 0:
      print("기간은 0보다 커야 합니다.")
    else:
      if "연이율" in message:
        value = value / 100
      break
  return value

principal = get_compund_rate("원금을 입력해 주세요")
rate = get_compund_rate("연이율을 입력해 주세요")
time = get_compund_rate("기간을 입력해 주세요")

# pow(): 제곱연산 - pow(a, b): a의 b제곱
total = principal * pow((1 + rate), time)
print(f"원금: {principal}, 이자율: {rate}, 기간: {time}, 최종 만기 금액: {total:.2f}원")