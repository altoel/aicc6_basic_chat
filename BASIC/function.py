# 함수는 def 키워드를 사용한다.

def my_func(na, age):
  print(" age is {1}, {0} hello".format(na, age)) # 포멧팅 순서대로 표시

# my_func("marshall", 20) # 호이스팅이 되지 않는다.
# my_func(na="marshall", age=21) # 키워드 파라미터

# arbitary arguments: 튜플로 여러 파라미터를 한번에 받는다.
def arb_func(*args):
  print(" age is {1}, {0} hello {2}".format(args[0], args[1], args[2]))

# arb_func("marshall", 20, "world")

# keyword arguments: 딕셔너리로 여러 파라미터를 한번에 받는다.
def key_arb_func(**kwargs):
  print(kwargs["name"])

# key_arb_func(name="marshall", age="20", city="incheon")

# 콜랙션 파라미터: 파라미터를 자료형 형태로 전달
def coll_func(aaa):
  for x in aaa:
    print(x)

# coll_func(["korea", "japan", "china"])
coll_func(("korea", "japan", "china"))