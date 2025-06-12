# 자료형: 리스트[], 튜플(), 딕셔너리{key: value}, 셋트{}

# 4. 셋트
# - 인덱스로 접근할 수 없다.
# - 내부 요소를 수정할 수 없다.
# - 중복된 요소를 포함할 수 없다. - 중복 요소가 있을 경우 오류가 나지는 않지만 데이터 표현은 되지 않는다.
# - 중괄호를 사용한다.

a = {"apple", "banana", "cherry", True, False}
# print(a) # 인덱스가 없고, 따라서 순서가 바뀐다.
# print(type(a))

# True = 1, False = 0, 1과 True가 중복되어 True가 표시
b = {True, 1, 2, 3}
# print(b)

# 길이
# print(len(a))

# 생성자
c = set(("apple", "banana", "cherry"))
# print(c)
# print(type(c))

# 반복문
for x in c:
  # print(x)
  pass

# 존재 여부
d = "apple" in a
# print(d)

# 요소의 추가
a.add("orange")
# print(a)

# 여러 요소를 합침
e = {"mango", "grape", "apple"} # 겹치는 요소는 하나만 표시
# a.update(e)
# print(a)

# 요소의 삭제
a.remove("apple")
# a.remove("grape") # 없는 요소 삭제 시 오류
a.discard("grape") # 없는 요소 삭제시 오류 발생 하지 않음
# print(a)

a.pop()
# print(a)

f = {"apple", "banana"}
g = {"apple", "cherry"}

# 두 개의 셋트를 하나의 변수에 담는다
h = f.union(g)
# print(h)

# 비운다
# f.clear()
# print(f)

# 차집합으로 합침
i = g.difference(f) # 앞의 셋트를 기준으로 중복 제거 후 표시
# print(i)

# 교집합
j = f.intersection(g)
# print(j)

# 교집합 여부 확인
print(f.isdisjoint(g)) # 교집합이 있으면 False, 없으면 True
