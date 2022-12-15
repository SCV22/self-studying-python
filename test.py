# #입력
# string = input("입력> ")

# #출력
# print("자료:", string)
# print("자료형:", type(string))

# string_a = input("입력A> ") #문자열 객체 선언
# int_a = int(string_a) #문자열을 숫자로 바꾸는 int를 이용한 객체 선언

# string_b = input("입력B> ")
# int_b = int(string_b)


# print("문자열 자료:", string_a + string_b)
# print("숫자 자료:", int_a + int_b)

# input_a = float(input("첫 번째 숫자> "))
# input_b = float(input("두 번째 숫자> "))

# print("덧셈결과:", input_a + input_b)
# print("뺄셈결과:", input_a - input_b)
# print("곱셉결과:", input_a * input_b)
# print("나눗셈결과:", input_a / input_b)

# #format() 함수로 숫자를 문자열로 변환하기
# string_a = "{}".format(10)

# #출력하기
# print(string_a)
# print(type(string_a))

# #And 연산자,  OR연산자
# print(True and False)
# print(True or False)

#입력을 받습니다.
# number = input("정수 입력>")
# number = int(number)

# # 양수 조건
# if number > 0:
#     print("양수입니다.")

# # 음수 조건
# if number < 0:
#     print("음수입니다.")

# # # 0 조건
# # if number == 0:
# #     print("0입니다.")

# #날짜/시간과 관련된 기능
# import datetime

# now = datetime.datetime.now()
# print(now.year, "년", now.month, "월", now.day, "일")

# # #오전 구분
# # if now.hour < 12:
# #     print("현재 시각은 {}시로 오전입니다.!".format(now.hour))

# # #오후 구분
# # if now.hour >= 12:
# #     print("현재 시각은 {}시로 오후입니다.!".format(now.hour))

#     #봄 구분
# if 3 <= now.month <= 5:
#     print("이번 달은 {}월로 봄입니다!".format(now.month))

#     #여름 구분
# elif 6 <= now.month <= 8:
#     print("이번 달은 {}월로 여름입니다!".format(now.month))

#     #가을 구분
# elif 9 <= now.month <= 11:
#     print("이번 달은 {}월로 가을입니다!".format(now.month))

#     #겨울 구분
# else:
#     print("이번 달은 {}월로 겨울입니다!".format(now.month))

# #입력
# number = input("정수입력>")
# number = int(number)

# #조건문사용
# if number % 2 == 0:
#     print("짝수")

# else:
#     print("홀수")

score = float(input("학점을 입력하세요!>>>"))

if 0 <= score <= 1:
    print("시대를 앞서가는 혁명의 씨앗")

elif 1.1 <= score <= 2.0:
    print("자벌레")

elif 2.1 <= score <= 3.1:
    print("플랑크톤")

else:
    print("사람입니다")


