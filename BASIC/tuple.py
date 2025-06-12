# 자료형: 리스트[], 튜플(), 딕셔너리{key: value}, 셋트{}

# 2. tuple
# - 값을 변경할 수 없다.
# - 중복 데이터를 허용한다.
# - 순서를 가지고 있다.
# - 데이터는 괄호를 사용한다.(생략 가능하지만 추천하지는 않는다.)
# - 모든 타입을 요소로 지정할 수 있다.

a = ("사과", "복숭아", "사과", 1, True)
b = ("apple")
c = "grape", "banana"

# print(a[0]) # 순서를 가지기 때문에 인덱싱이 된다.
# print(b) # 요소가 하나일 경우 괄호가 생략되어 표시
# print(c) # 생략된 괄호는 만들어서 표시

# a[0] = "포도" # 요소 변경시 오류
# print(a)

# print(type(a))
# print(type(b)) # 하나의 요소로 표시된 경우 문자열 타입
# print(type(c))

# 개수 확인
# print(len(a))

# 생성자로 튜플 생성
b = tuple(("사과", "배", "딸기"))
# print(b)

# 튜플 슬라이싱
# print(a[1:3])

# 반복문 읽기
for x in a:
  # print(x)
  pass

# if문으로 존재 여부 확인
if "사과" in a:
  # print(True)
  pass

# 요소의 변경
b = list(a)
b[0] = "포도"

c = tuple(b)
# print(c)

# 요소의 추가
# a.append("라임") # 추가 안됨
# print(a)
b.append('라임')
c = tuple(b)
# print(c)

# 튜플 자체에 요소 추가
a += ("라임", "레몬")
# print(a)

# 구조분해 할당
(a1, a2, a3, a4, a5, a6, a7) = a

# print(a5)

# 요소의 범위
# print(range(len(a)))

for i in range(len(a)):
  # print(a[i])
  pass

# 튜플 복사하여 붙이기
print(a * 2)
