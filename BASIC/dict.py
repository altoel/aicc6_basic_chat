# 자료형: 리스트[], 튜플(), 딕셔너리{key: value}, 셋트{}

# 3. 딕셔너리
# - 중복을 허용하지 않는다.
# - 변경 가능
# - 키와 값의 쌍으로 구성(자바스크립트의 객체와 유사)

a = {
  "name": "marshall",
  "age": 20,
  "address": "Incheon",
  # "address": "Seoul", # 중복키가 있을 경우 마지막 키값만 적용
  "gu": ["bupyeung", "namgu", "jungu"]
}

# print(a)
# print(type(a))

# 길이
# print(len(a))

# 요소의 접근
# print(a["name"])
# print(a["gu"][0])

# 생성자로 생성
b = dict(name="john", age=30)
# print(b)

# 키 값으로 접근(get)
# print(a.get("age"))

# 키값만 출력
# print(a.keys())

# 요소의 변경
a["age"] = 30
a.update({"name": "jane"})
# print(a)

# 요소의 추가
a["color"] = ["red", "green", "blue"]
a.update({"number": [1, 2, 3]})
# print(a)

# 요소의 제거
# c = a.pop("age")
# print(a)
# print(c)

a.popitem() # 마지막 요소 삭제
# print(a)

a.clear()
# print(a)

d = {
  "name": "marshall",
  "age": 20,
  "address": "Incheon",
  # "address": "Seoul", # 중복키가 있을 경우 마지막 키값만 적용
  "gu": ["bupyeung", "namgu", "jungu"]
}

# keys를 출력
for x in d.keys():
  # print(x)
  pass

for x in d.values():
  # print(x)
  pass

# 키와 값을 튜플로 묶어서 출력
# print(d.items())

for key, value in d.items():
  print(key, value)
  print(type(key), type(value)) # 반복문으로 추출된 데이터는 원래 타입을 갖는다.

# 딕셔너리 내부의 딕셔너리
family = {
  "first": {
    "a": "marshall",
    "b": "james"
  },
  "second": {
    "c": "jane",
    "d": "john"
  }
}
print(family["second"]["c"])