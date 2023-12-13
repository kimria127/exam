#<오픈소스프로그래밍 기말 프로젝트>
#
# ● 아래의 코드를 수정 혹은 프로그래밍하여 문제를 해결하시오.
# ● 문제의 점수는 각각 표시되며, 부분점수가 존재합니다.
#
# 학번 : 20201860 이름 : 김리아

import os
import time

# Q.1 10점
#
# 문자열 my_string과 target이 매개변수로 주어질 때,
# target이 문자열 my_string의 부분 문자열이라면 1을,
# 아니라면 0을 return 하는 solution 함수를 작성하시오.
#
# 제한사항
# 1 ≤ my_string 의 길이 ≤ 100
# my_string 은 영소문자로만 이루어져 있습니다.
# 1 ≤ target 의 길이 ≤ 100
# target 은 영소문자로만 이루어져 있습니다.

def solution(my_string, target):
    1 <= len(my_string) <= 100
    1 <= len(target) <= 100
    # target이 my_string의 부분 문자열일 경우
    if target in my_string:
        answer = 1   #answer에 1을 반환하고
    else: # 부분 문자열이 아닐경우 
        answer = 0 #answer에 0을 반환한다

    return answer 

#my_string과 target 문자열을 지정
my_string = "kimria"
target = "kria" 
result = solution(my_string, target) #solution 함수 호출
print(result)



# Q.2 10점
#
# 모스부호 해독 프로그램 만들기
# 문자열 letter 가 매개변수로 주어질 때,
# letter 영어 소문자로 바꾼 문자열을 return 하는
# solution 함수를 완성하시오.
#
# 제한사항
# 1 ≤ letter 의 길이 ≤ 1,000
# letter 의 모스부호는 공백으로 나누어져 있습니다.
# letter 에 공백은 연속으로 두 개 이상 존재하지 않습니다.
#
# letter = 여러분의 좌우명 또는 인상 깊었던 말을 쓰시오.

def solution(letter):
    morse_to_char = {
        '.-': 'a', '-...': 'b', '-.-.': 'c', '-..': 'd', '.': 'e',
        '..-.': 'f', '--.': 'g', '....': 'h', '..': 'i', '.---': 'j',
        '-.-': 'k', '.-..': 'l', '--': 'm', '-.': 'n', '---': 'o',
        '.--.': 'p', '--.-': 'q', '.-.': 'r', '...': 's', '-': 't',
        '..-': 'u', '...-': 'v', '.--': 'w', '-..-': 'x', '-.--': 'y',
        '--..': 'z'
    }
    1 <= len(letter) <= 1000
    words = letter.split(' ') # letter문자열을 공백을 기준으로 나눠 반환함
    answer = '' #answer변수 초기화 
    if '  ' in letter:
        return "공백이 연속으로 존재함"

    for word in words: #각 단어에 대해 모스코드를 영어로 변환하여 결과에 추가
      if word in morse_to_char: #만약 모스코드가 morse_to_char내에 존재한다면
        answer+=morse_to_char[word] # 해당하는 알파벳을 answer에 추가
      else: #존재하지 않으면
        answer+=' ' #공백으로 처리
    return answer

letter = "-.- ... ...- --. ..- -- .--- ..- --. . ...- .--. ." #' 열심히 살자' 라는 문장의 모스부호를 letter에 저장
result = solution(letter) 
print(result) #함수 호출 및 출력



# Q.3 10점
#
# 행성의 나이를 알파벳으로 표현할 때,
# a는 0, b는 1, ..., j는 9
# 예를 들어 cd는 23살, fb는 51살입니다.
# age가 매개변수로 주어질 때
# PROGEAMMER-857식 나이를 return 하도록
# solution 함수를 완성하시오.
#
# 제한사항
# age는 자연수입니다.
# age ≤ 1,000
# PROGRAMMERS-857 행성은 알파벳 소문자만 사용합니다.

def solution(age):
    age <= 1000
    base = ord('a') # 문자 'a'의 아스키코드 값을 구한다. 0에 대응..

    answer = '' # 변수 초기화
    while age > 0:  #나이의 각 자릿수별 변환
        remainder = age % 10 #age의 가장 낮은 자릿수를 구한다 
        answer = chr(remainder + base) + answer # 현재 자릿수를 문자로 변환하여 answer에 추가
        age //= 10 # 현재자릿수를 제거하고 다음 자릿수를 변환.

    return answer

age = 63 #나이를 63세로 지정
result = solution(age)
print(result) #함수 호출 및 출력 



# Q.4 10점
#
# x축과 y축으로 이루어진 2차원 직교 좌표계에 중심이 원점인
# 서로 다른 크기의 원이 두 개 주어집니다.
# 반지름을 나타내는 두 정수 r1, r2가 매개변수로 주어질 때,
# 두 원 사이의 공간에 x좌표와 y좌표가 모두 정수인 점의 개수를
# return하도록 solution 함수를 완성해주세요.
# ※ 각 원 위의 점도 포함하여 셉니다.
#
# 제한사항
# 1 ≤ r1 < r2 ≤ 1,000,000

def solution(r1, r2):
    answer = 0 #변수 초기화 
    1 <= r1 < r2 <= 1000000
    distance = (r1 + r2) # 두 원의 중심 사이의 거리를 구함

    if distance >= r1 and distance >= r2:     # 두 원이 겹치는 경우 
        for x in range(-r1, r1 + 1):
            for y in range(-r1, r1 + 1):  #x와 y에 -r1~r1사이의 정수 순차대입 
                if x**2 + y**2 <= r1**2: #만약 (x, y)가 r1원 내부에 속하고
                  if x**2 + y**2 <= r2**2: #r2원 내부에도 속한다면
                    answer += 1 #answer을 1 증가시킨다

    return answer

r1 = 2 
r2 = 3 #두 원의 반지름 지정
result = solution(r1, r2)
print(result) # 함수 호출 및 출력



# Q.5 10점
#
# 0 또는 양의 정수가 주어졌을 때,
# 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.
#
# 예를 들어, 주어진 정수가 [6, 10, 2]라면
# [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고,
# 이중 가장 큰 수는 6210입니다.
#
# 0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때,
# 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어
# return 하도록 solution 함수를 작성해주세요.
#
# 제한사항
# numbers의 길이는 1 이상 100,000 이하입니다.
# numbers의 원소는 0 이상 1,000 이하입니다.
# 정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.
#
# numbers = [8, 30, 17, 2, 23]

def solution(numbers):
    answer = '' # 변수 초기화
    numbers_str = list(map(str, numbers)) # numbers를 문자열로 변환해 리스트로 저장
    numbers_str.sort(key=lambda x : str(x)*3, reverse=True) # 크기 비교를 세번 수행해 비교해서 내림차순으로  정렬 
    if numbers_str[0] == '0': #리스트의 첫 번째 원소가 0이면 
       return '0' #'0'을 반환
    answer = ''.join(numbers_str) #문자열을 이어붙여 가장 큰 수를 만들어 answer에 저장

    return answer

numbers = [8, 30, 17, 2, 23] 
result = solution(numbers)
print(result) # 함수 호출 및 출력