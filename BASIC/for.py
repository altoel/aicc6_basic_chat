# 파이썬에서는 주로 for in문을 사용
my_list = ["a", "b", "c", "d", "e", "f", "g"]

for x in my_list:
  if x == "c":
    # break: 조건에 맞으면 중단
    # continue: 존건에 맞는 부분 건너뜀
    pass
  # print(x)

# range(): 숫자의 범위 생성
for k in range(10):
  # print(k)
  pass

for y in range(3, 10, 2): # 3 ~ 10까지 2씩 증가
  # print(y)
  pass

# 구구단: 중첩 for문
for i in range(2, 10):
  print(f"---------{i}단---------")
  for j in range(1, 10):
    print(f"{i} * {j} = {i * j}")


    
    