#list tuple set dictionary - 특징 메소드(저장, 수정, 삭제) 

#함수 모듈 예외 


#매개변수 없는 함수
def hello_3times():
    print("hello");
    print("hello");
    print("hello");
    
#실행
print(hello_3times()); #리턴값이 없어서 None으로 표현 (파이썬) / undefined (자바스크립트) Null (자바)
hello_3times();





#매개변수 있는 함수 정의1 
def message_3times(message):
    print(message);
    print(message);
    print(message);

#실행
#print(message_3times()); #None (리턴값 미 존재)
#message_3times(python);
#message_3times(python, 3); #오류
#자바, 파이썬 - 매개변수 갯수 일치해야.
#자바스크립트 매개변수 남아도 가능 알아서 처리


#매개변수 있는 함수 정의2
def message_ntimes(message, n):
    #type(n) == 'int'
    for i in range(1, n+1, 1): #n번까지 
        print(message);
    
#실행
message_ntimes("python", 5);
#message_ntimes(5, "python");



#기본값이 있는 매개변수 있는 함수 정의
def basic_ntimes(message="java", n=5):
    # type(n) == 'int'
    for i in range(1, n+1, 1):
        print(message);
        
#실행
#basic_ntimes();
basic_ntimes(message="js", n=10); #키워드매개변수 
basic_ntimes(n=10, message="python"); #순서 상관 없
#basic_ntimes(5, "python");

#예
#print(10, 20) #sep = ' -  ' end=' : ' 
#print(100, 200) 


#가변매개변수 (갯수가)  -  1개만 가능
#일반 매개변수 뒤에만 선언 되어야.
def dynamic_message(n, *msg): #하나의 매개변수에 여러값을 받는 형태 (1개, 여러개도)
    for i in msg:
        print(i)
    #print(type(msg));


dynamic_message("python", 4);
dynamic_message(4, "python");
dynamic_message("python", "java");
dynamic_message("python", "css", "spring");

'''
#가변 매개변수 함수 정의 
def dynamic_ntimes(*msg): #tuple 타입 (값 변경 불가능한 리스트) 
    n=3 ;
    for i in range(1, n+1, 1):
        print(msg)
            #컴파일 오류 없음 

#실행
dynamic_ntimes("spring", "java")
dynamic_ntimes("spring") #("spring", ) #튜플이라는 뜻 
dynamic_ntimes("spring", 1, "python", True, 2.5)
'''



#가변 매개변수 함수 정의 
def dynamic_ntimes(*msg, n=10): #n 기본값 설정
    for i in range(1, n+1, 1):
        print(msg)
            #컴파일 오류 없음 

#실행
dynamic_ntimes("spring", "java", 3, n=5 ) #ok
dynamic_ntimes("spring") 
dynamic_ntimes("spring", 1, "python", True, 2.5)


#기본값 매개변수, 키워드 매개변수, 가변 매개변수, 일반 매개변수

#함수 - 입력값(매개변수) - 기능 구현 문장 - 리턴값 


#리턴값 정수 함수 정의 
def return2_func():
    print("리턴 전");
    return 0; 

#실행
r2 = return2_func();
print(r2)


#리턴값 없는 함수 정의 
def return3_func():
    print("리턴 전");
    return ; #함수 중단 
    print("리턴 후")
    
#실행
r2 = return3_func();
print(r2) #리턴값이 없어서 None



#리턴값 여러개면 자동 tuple 함수 정의 
def return4_func():
    print("리턴 전");
    return 1, 2, 3, 4, 5; #tuple #값변경불가 #함수에 주로 같이 쓰임 

#실행
r2 = return4_func();
print(r2) #(1, 2, 3, 4, 5)
print(type(r2))

print(r2[0])
#r2[0] =10 ; #error


#리턴값 여러개면 수동 list 함수 정의 
def return4_func():
    return [1, 2, 3, 4, 5]; #list  

#실행
r2 = return4_func();
print(r2) #(1, 2, 3, 4, 5)
print(type(r2))

print(r2[0])
r2[0] =10 ; 

'''
#리턴값 여러개면 수동 set 함수 정의 
def return4_func():
    return {1, 2, 3, 4, 5}; #set  

#실행
r2 = return4_func();
print(r2) #(1, 2, 3, 4, 5)
print(type(r2))


#리턴값 여러개면 수동 set 함수 정의 
def return4_func():
    return {1:1, 2:2, 3:3, 4:4, 5:5}; #set  

#실행
r2 = return4_func();
print(r2.items()) #(1, 2, 3, 4, 5)
print(type(r2))
'''


#매개변수 / 지역변수 / 전역변수

a = "전역변수"; #외부
#이 아래는 내부에 존재
#지역변수는 함수가 진행되는 동안에만 메모리에 머물러, 함수에 출력 
def vartest(b): #b와 c는 vartest 내부에서만 
    global a #있으면 a= 전역변수, 없으면 a= 매개변수 
    a = "전역변수 값 수정" 
    c = "지역변수";
    print(a); 
    print(b);
    print(c); #들여쓰기 중요 

def vartest2(d): #d와 e는 vartest2 내부에서만 
    e = "다른 지역변수";
    print(a);
    print(d);
    print(e);

vartest("매개변수1")
vartest2("매개변수2")
print(a);
#print(c); #오류
#print(e); #오류

global_var = 0
def inc():
    local_var = 1;
    local_var = local_var + 1;
    global global_var
    global_var = global_var +1;
    print("지역변수 {} 값, 전역변수 {} 값입니다".format(local_var, global_var) );
    
inc();
inc();
inc();
inc();
inc();


#재귀호출

#5! = 5 * 4 * 3 * 2 * 1
#팩토리얼을 구하는 방법
#반복문 팩토리얼 함수1

def fact1(n):
    result = 1;
    for i in range(1, n+1, 1):
        result = result * i; 
        print("{}!={}입니다".format(i,result));
    return result;

r1 = fact1(5);
print(r1);



#재귀호출 팩토리얼 함수2 - #5! = 5*4!  $! = 4*3! 2! 1!
# 1> 반드시 리턴값이 존재할 것
# 2> 함수 종료 조건 필수 만들 것 (무한루프 이므로 - if n ==?: return ?; )
def fact2(n):
    if n == 0 :
        return 1;
    else :
        result = n * fact2(n-1);
        print("{}!={}입니다".format(n,result));
        return result;

r2 = fact2(5);
print(r2);

#자바 스크립트와 파이썬 함수 변수 취급
#함수 매개변수, 지역함수, 리턴함수

def f1():
    print("출력");

import time
def call_func(f):
    #f 함수이면 5초 후에 실행
    time.sleep(5)
    f()

call_func(f1);

#map 함수 (함수, 리스트 ) - mapping

a = [2.5, 4.7, 3.6, 3.4]
print(a);
a = list(map(int, a))
print(a);

b = ["java programming 과정", "oracle sql", "spring framework", "python programming"];
#첫 문자만 대문자, 포함된 모든 문자 대문자 변경
#앞의 4개의 문자들만 대문자로 변경

def my_upper(s):
    #문자열
    return s[ :4].upper() + s[:4]; 

print(my_upper("java programming 과정"))

b = list(map(my_upper, b))
print(b);


def no_action():
    pass

no_action();

#람다식 - 매개변수와 리턴문만 가지는 무명의 함수 /정의 + 호출 동시에
def lan1():
    return 0;

print(lan1());

print ((lambda  : 0)())
#매개변수 : 리턴값 
print ((lambda x  : x*x )(10))
print ((lambda x, y : (x+y, x-y, x*y, x/y) )(10, 2))


'''
#모듈 - basic.py 파이썬 소스 파일 = 모듈
#파이썬 내장 다른 모듈 math.py : a()


import math
a = 3
b = 2
print("math.pow(a,b)=", math.pow(a,b))
print("math.trunc(a,b)=", math.trunc(a/b))

#파이썬 기본 내장 함수
print("math.abs(-10)=", abs(-10))
print("math.round(a/b)=", round(a/b))

#파이썬 기본 내장 함수 확인 
print(dir(__builtins__))
print(dir(a)) #str 타입 포함 함수 목록 확인
'''
