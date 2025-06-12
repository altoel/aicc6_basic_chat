import re
from words import hangman_words
import random

hangman_art = {0: ("   ",
                   "   ",
                   "   "), 
               1: (" o ",
                   "   ",
                   "   "),
               2: (" o ",
                   " | ",
                   "   "),
               3: (" o ",
                   "/| ",
                   "   "),
               4: (" o ",
                   "/|\\",
                   "   "),
               5: (" o ",
                   "/|\\",
                   "/  "),
               6: (" o ",
                   "/|\\",
                   "/ \\"),}

# for line in hangman_art[6]:
#   print(line)

test_word = ("dog", "lion")

# 한글 입력 체크 함수
def check_kor(text):
  p = re.compile('[ㄱ-힣]')
  r = p.search(text)
  if r is None:
    return False
  else:
    return True

# 행맨 그리기 함수
def display_hangman(wrong_guesses):
  print("*****************")

  for line in hangman_art[wrong_guesses]:
    print(line)

  print("*****************")

# 행맨 힌트 출력 함수
def display_hint(hint):
  print(" ".join(hint))

# 정답 출력 함수
def display_answer(answer):
  print(" ".join(answer))

# 메인 함수
def main():
  is_run = True
  wrong_guesses = 0
  answer = random.choice(hangman_words)
  guessed_letters = set()
  hint = ["_"] * len(answer)

  while is_run:
    display_hangman(wrong_guesses)
    display_hint(hint)
    # display_answer(answer)

    guess = input("문자를 입력하세요: ").lower()

    if check_kor(guess):
      print("한글은 입력할 수 없습니다.")
      continue
    if len(guess) != 1 or not guess.isalpha():
      print("영문자 하나만 입력해 주세요")
      continue
    if guess in guessed_letters:
      print("이미 입력한 문자 입니다.")
      continue

    guessed_letters.add(guess)

    if guess in answer:
      for i in range(len(answer)):
        if answer[i] == guess:
          hint[i] = guess
    else:
      wrong_guesses += 1

    if "_" not in hint:
      display_hangman(wrong_guesses)
      display_answer(answer)
      print("YOU WIN!!")
      is_run = False
    elif wrong_guesses >= len(hangman_art) - 1:
      wrong_guesses = len(hangman_art) - 1
      display_hangman(wrong_guesses)
      display_answer(answer)
      # display_answer(answer)
      print("YOU LOSE!!")
      is_run = False

# 프로그램 시작
if __name__ == "__main__":
  main()