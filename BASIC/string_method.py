# 문자열 조작을 위해 만들어진 메서드
# isalpha(): 문자열이 모두 알파벳인지 확인
a = 'abc'
b = "ABC"
c = "a b c"
d = "abc123"

# print(a.isalpha())
# print(b.isalpha())
# print(c.isalpha())
# print(d.isalpha())

# isnumeric(): 문자열이 모두 숫자인지 확인
# e = 123
f="123"
g="12 3"

# print(e.isnumeric())
# print(f.isnumeric())
# print(g.isnumeric())

# isalnum(): 문자열이 숫자 또는 알파벳인지 확인
h = "123"
i = "abc"
j = "123abc"
k = "123 abc"

# print(h.isalnum())
# print(i.isalnum())
# print(j.isalnum())
# print(k.isalnum())

# join(): 문자열을 연결하여 새로운 "문자열" 반환
my_list = ["aa-bb-cc", "dd-ee-ff", "gg-hh-ii"]
rs = "/".join(my_list)
# print(rs)

my_tup = ("aa", "bb", "cc")
rs_tup = "-".join(my_tup)
# print(rs_tup)

# startswith(): 문자열이 특정 문자로 시작하는지 확인
m = "Hello, my name is marshall"
m1 = m.startswith("H")
print(m1)

# endswith(): 문자열이 특정 문자 또는 문자열로 끝나는지 확인
m2 = m.endswith('ll')
print(m2)

# https://www.w3schools.com/python/python_ref_string.asp