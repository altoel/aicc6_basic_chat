# 자료형: 리스트[], 튜플(), 딕셔너리{key: value}, 셋트{}
# 1 list
a = ["사과", "배", "딸기", "포도", "사과", "포도", "체리", "수박"]
# print(a) # 중복 허용

# 슬라이싱
# print(a[:3])
# print(a[3:])
# print(a[-1])
# print(a[::2])

# 마지막 요소 추가
a.append('라임')
# print(a)

# 특정 위치에 요소 추가
a.insert(2, '라임')
# print(a)

# 파라미터에 지정된 요소 삭제
a.remove("라임")
# print(a) # 중복될 경우 앞에 있는 요소 하나만 삭제

# 마지막 요소 삭제
a.pop()
# print(a)

m = a.pop(2)
# print(m) # 삭제된 요소를 변수에 저장할 수 있다.
# print(a)

# 리스트 비우기
a.clear()
print(a)

b = ["사과", "배", "딸기", "포도", "사과", "포도", "체리", "수박"]

# 반복문으로 읽기
for x in b:
  # print(x)
  pass

# 정렬
b.sort()
# print(b)

# 역정렬
b.sort(reverse=True)
# print(b)

# 복사
# c = b.copy()
# c[0] = "라임"
# print(c)
# print(b)

c = list(b)
c[0] = "라임"
print(c)
print(b)

# 리스트 합치기
d = ["list1", "list2"]
# e = b + d
# print(e)

# for x in d:
#   b.append(x)

# print(b)

b.extend(d)
# print(b)

# 갯수 확인
print(b.count("사과")) # 지정 요소 갯수
print(len(b)) # 전체 갯수