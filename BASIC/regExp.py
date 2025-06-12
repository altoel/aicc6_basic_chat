# 정규표현식이란 문자열을 처리하는 방법 중의 하나로 특정한 조건의 문자를 '검색'하거나 '치환'하는 과정을 매우 간편하게 처리할 수 있도록 하는 수단이다.

import re # 정규표현식 사용 모듈

a = "I live in Korea, Incheon 16"
b = re.search("^I.*Incheon$", a) # ^(시작) I로 시작하고 $(종료) Incheon으로 끝나는 문자열 검색
# print(b)

# findall(): 매칭되는 모든 문자열을 리스트 형태로 리턴
c = re.findall('[a-zA-Z0-9]', a)
d = re.findall("\d", a) # 숫자 검색(digit)
e = re.findall("K...a", a) # K로 시작하고, 중간에 3글자 있고, a로 끝나는 문자열
print(e)

f = re.findall("K.*a", a) # K로 시작하고 a로 끝나는 문자열 추출 : zero or more
g = re.findall("Kore.+a", a) # Kore와 a 사이에 어떤 문자가 1개 이상 있는 문자열 추출 Korema, koremoa... 등으로 수정하면 찾을 수 있음 : one or more
h = re.findall("Kore.?a", a) # zero or one : Korea, Koreaa 등으로 수정하면 찾을 수 있음 : Koreaaaaa는 찾을 수 없음
# print(f)
# print(g)
# print(h)
i = re.findall("K.{3}a", a)
j = re.findall("live|Korea", a) # live 또는 Korea가 있는 문자열 추출
# print(i)
print(j)


# special sequences는 \문자로 시작한다.
import re

a = "amarshall lives in Korea, Incheon 13"
b = re.findall(r"\Amarshall", a) # \A : 문자열 문장의 시작과 매칭. r을 빼면 warning 발생

if b:
  print("Matched")
else:
  print("Not matched")

c = re.findall(r"marshall\B", a) # marshall 문자열이 뒤에 오지 않으면 매칭 : marshall 뒤에 s가 있으므로 매칭 amarshalls 도 매칭. 뒷 부분에 marshallize가 있게 되면 두개를 매칭. amarshall은 매칭이 안됨.
# print(c)

d = re.findall(r"\Bmarshall", a) # marshall 문자열이 앞에 오지 않으면 매칭 : marshall 앞에 a가 있으므로 매칭. marshalla와 같이 marshall이 앞에 오면 매칭이 안됨.
# print(d)

e = re.findall(r"\bmarshall", a) # marshall 문자열이 단어의 시작에 오면 매칭 : marshall이 단어의 시작에 있으므로 매칭. marshalla와 같이 marshall이 단어의 시작에 오지 않으면 매칭이 안됨. amarsahll은 매칭이 안됨.
# print(e)

f = re.findall(r"marshall\b", a) # marshall 문자열이 단어의 끝에 오면 매칭 : marshall이 단어의 끝에 있으므로 매칭. marshalla와 같이 marshall이 단어의 끝에 오지 않으면 매칭이 안됨. amarsahll은 매칭이 안됨.
# print(f)

g = re.findall(r"\d", a) # 숫자를 찾음
# print(g)

h = re.findall(r"\D", a) # 숫자가 아닌 것을 찾음 : 공백, 문자, 특수문자 등 포함
# print(h)

i = re.findall(r"\s", a) # 공백을 찾음
# print(i)

j = re.findall(r"\w", a) # 문자와 숫자를 찾음
# print(j)

k = re.findall(r"13\Z", a) # 문자열 문장의 끝과 매칭
# print(k)

l = re.findall(r"13$", a) # 문자열 문장의 끝과 매칭
print(l)


import re

a = "marshall lives in Korea, Incheon 13 12:59 234"
b = re.findall("[img]", a) # i, m, g 중 하나라도 있으면 매칭
# print(b)

c = re.findall("[a-c]", a) # a부터 z까지 중 하나라도 있으면 매칭 : [a-zA-z0-9 ] - 대문자, 소문자, 숫자, 공백 중 하나라도 있으면 매칭
# print(c)

d = re.findall("[^a-zA-Z]", a) # : [^] - ^가 대괄호 안에 있으면 not을 의미. 대괄호 안에 있는 문자를 제외한 나머지 문자를 매칭
# print(d) # [' ', ',', '1', '3'] - 대문자, 소문자를 제외한 나머지 문자를 매칭

e = re.findall("[0-9][0-9]", a) # [0-9] - 숫자 중 하나라도 있으면 매칭 : 숫자 두개 묶 찾음
# print(e) # ['12', '59', '23'] - 숫자 두개 묶음을 찾음 [0-9][0-9][0-9] : 숫자 세개 묶음을 찾음

f = re.search(r"\s", a) # \s - 공백 문자를 매칭 : 객체를 반환
# print(f)

g = re.search(r"live", a)

# span 위치 출력
# print(g.start())
# print(g.end())

# <re.Match object; span=(8, 9), match=' '> 8, 9번째 인덱스에 공백 문자가 있음

h = re.split(r"\s", a, 1) # \s - 공백 문자를 기준으로 문자열을 나눔 : 3번 파라미터는 나눌 횟수, 나누는 기준은 첫번째 공백 문자
# print(h)

i = re.sub(r"\s", ":", a) # \s - 공백 문자를 :로 대체
print(i)

