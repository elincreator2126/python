#변수 연산자 조건문 반복문 문법
#자바 int i = 10;
#자바 스크립트 let j = 20

k = 30
print(type(k))
k=  3.14
print(type(k))
k= True
print(type(k))
k= 'abc'
print(type(k))
k = None 
print(type(k))

#파이썬 1개 값 저장 변수 타입 - int float bool str Nonetype
#숫자 연산자
a= 10
b =3
print("a/b=" , a/b) #실수 몫
print("a//b=" , a//b) #정수 몫
print("a$b=" , a/b) #정수 몫 구한 이후 나머지
print("a를 2진수로=" , bin(a))
print("a를 16진수로=" , hex(a))
print("a를 8진수로=" , oct(a))
print("3.14-3.04=" , 3.14-3.04) #오차범위     

#문자 연산자
a = "abcdefg"
b = 'def'
c= 100
print(a+b) #문자결합
print(a*3) #문자*int 문자를 int 반복 

d = '''모듈 - basic.py 파이썬 소스 파일 = 모듈 파이썬 내장
다른 모듈
math.py : a()'''
print(d)

print(a[2:4]) #2번 인덱스부터 4번인덱스 이전까지 부분문자열
#(:) => 슬라이싱연산자

print(a[2: ]) #2번 인덱스부터 나머지인덱스 이전까지 부분문자열
print(a[ :4]) #0번 인덱스부터 4번인덱스 이전까지 부분문자열
print(a[-1:4])

a = "multicampus"
#a cam 이라는 문자 포함여부
#찾으려는 문자열 in 타겟이 되는 문자열 - bool 
print ('cam' in a) #in은 포함여부만 알려주는 것 
# a cam 위치 몇 번 인덱스니
# 함수
print(a.find('cam'))
print(a.rfind('cam'))

#a변수에서 'cam'문자열부터 나머지 문자열 출력 
print(a[a.find('cam'):])

print(a.count('m')) #m문자 갯수
print(len(a)) #총 문자 갯수
print(dir(a)) #str 타입 포함 함수 목록 확인

a="multi";
b="python";
c=100; #str타입변경
print("{}는 정수이고  {} 는 문자열입니다".format(c, a));

print("{:+10.2f}".format(10/3)); #3.33
print("{:+10d}".format(10//3)); #3



#10//3, math.trunc(10/3) round(10/3)

#함수/실수 -> 문자열로 
print(type(100)) #int
print(type(str(100))) #str

print("abc" + "def" + str(100))


'''
#문자열 -> 실수
#파이썬 키보드 입력 
in2 = input('정수 1개를 입력하세요')
#print(int(in2)  );

fo2 = input('실수 1개를 입력하세요')
print( float(fo2) + int(in2) );

bo2 = input('논리값  1개를 입력하세요')
print( bool(bo2));
#bool(TRUE, true, .....0)  어떤 값이든 상관없이 입력된 데이터가 있으면 true 이다. 
'''

# main(String [] args) - 100 200 300 역할을 파이썬에서 해보자
'''
import sys
print(sys.argv[1])
print(sys.argv[2])
print(sys.argv[3])
'''
#['C:/kdigital/python_source/basic.py', 'python', '100', '3.14']
#0번 인덱스는 값이 아니라 다른 것이 출력되므로





#파이썬 여러개 데이터 저장 타입 - 리스트
#리스트 = 자바 동적 배열 / 여러가지 타입 리스트 
#파이썬 여러 타입의 데이터를 저장해서 일렬 
#: 슬라이싱 연산자 그대로 사용 [0] + * in 


a2 = [1, 2, 3, 4 ,5] #list
a = ["title", 30, 45000.99, True, [90, 80, 70] ]
print(type(a))
print(a[0])
print(a[1:3])
print(a + a2)
print(a2 * 5)
print(1 in a2) #True


print(len(a)) #5

print(len(a[4])) #3


a.append(100); 
#a[5] = 100; #error
print(len(a)) #6
#a[100] = 100
print(a[5]);


a.insert(1, 200); #추가
print(len(a)); #7
print(a[1]);

print(a);
#a = ["title",200,  30, 45000.99, True, [90, 80, 70], 200 ]

#print(len(a[5]) #6


a[1] = 300; #index 존재하면 변경/ 미 존재 시, 오류
print(a);


a.pop() #리스트 마지막 데이터 삭제
print(a);
a.remove(30); #존재하는 데이터 삭제 
print(a);
#a.remove(3000); #존재하지 않는 데이터 삭제 오류
#print(a);

del a[0]; #0번 인덱스 데이터 삭제
print(a);


a2.sort();
#print(a2.sort()); #sort함수 정렬. 리턴값이 없음
#(파이썬에선 값이 없는 것이 None으로 표현)
print(a2);

a2.reverse(); #내림차순 정렬 
print(a2);

#a.sort(); #오류, #리스트에 리스트 또 정렬 불가 
#print(a);

#튜플. 값을 변경(추가 삭제 수정)할 수 없는 리스트
#함수 리턴값 - 여러개 튜플

#tuple 소괄호 모양 
print(type(d))
print(d[0])

#d[0] = 100;
#del d[0];
#d,append(6);

#() 없는 튜플  => 언패킹
a = 1, 2, 3, 4 ,5 ;
print(a);
print(type(a))

a,b = 1, 2
print(a);
print(b);

#리스트와 튜플 - 인덱스 저장 순서 있다. 


#셋 - 인덱스 없다. value만 있다. 중복 데이터 없다. 
b= {1, 2, 3, 4 ,5, 5} #set
print(type(b))

b.add(5)
print(len(b))
print(b)

#딕셔너리=자바 map(key, value) 쌍 데이터 모음
#-인덱스 없다. 중복되지 않는 key 
c = {'name':'lee', "2":200, 'id':'lee'} #dict
print(type(c)) #dict

print(c.items())
#dict_items([('name', 'lee'), ('2', 200), ('id', 'lee')])
print(c.keys())
#dict_keys(['name', '2', 'id'])
print(c.values())


#in
print('id' in c) #True
c['id']='python'; #id key 값 변경 수정
c['email']='all.com'; #email 값 추가

print(c.items())

d = {'seq': 1, 'title':'제목', 'contents':'내용',
     'addfiles':["a.png", "b.png", "c.ppt"]}
print(d['addfiles'][0])

#'contents' in d 
d.pop('contents') #key와 value 한 쌍으로 삭제 
print(d.items())



#포함 여부확인 데이터  in 문자열 |리스트 | 셋|튜플 |딕셔너리 
#int float str bool None
# list set tuple dict
#[] { } ( )  {1:1}

#함수
#6장 - 조건문 반복문 함수 클래스 - "들여쓰기"
# 조건 - bool - True . False - 비교연산, 
if 10 <= 5 :
    print(1)
    print(100)
else :
    print(2)
    print(200)

#a변수에 사용자 입력값 저장, 0이면 프로그램 종료하고
    #아니면 3 / a 출력
'''
a = input();
a = int(a) 
if a == 0 :
    print("0으로 나누기 불가")
    print("프로그램 종료")
else :
    print("3을 {}로 나눈 결과는 {}입니다." .format(a, 3 /a));
'''    
#switch-case 파이썬
    
#a변수에 사용자 입력값 저장, 0이면 프로그램 종료하고
    #아니면 3 / a 출력

#run con ... - 80 70 60 
'''
import sys #customized run으로 실행해야 함. (매개값 직접 입력 후 실행)
print(sys.argv[1])
print(sys.argv[2])
print(sys.argv[3])

kor = int(sys.argv[1]);
mat = int(sys.argv[2]);
eng = int(sys.argv[3]);

total = kor + mat + eng;
avg = total / 3;

if avg >= 90 :
    grade = "A";
elif avg >= 80: 
    grade = "B";
elif avg >= 70:
    grade = "C";
elif avg >= 60:
    grade = "D";
else :
    grade = 'P';

print(grade);
'''

##실습 - 조건문 활용
#num 짝수인지 홀수 인지 검사1
#짝수이면 짝수이다. 홀수이면 홀수이다. 
#num = ?; 

import random
#num = random.randint(1, 100) # 1<=?<=100
num = random.randrange(1, 101) # 1<=?<101
print(num)

if num % 2 == 0 :
    print("짝수");
else :
    print("홀수");

#num (문자열 타입) 짝수인지 홀수인지 검사2
    '''
num = input("정수 입력하세요") #123456
#print(num)
num = num[len(num) - 1 ] #6



if num in "02468" :
    print("짝수");
elif num in "133579" :
    print("홀수");
else :
    print("정수 형태의 데이터가 아닙니다.");
'''

#리스트
#while 조건식 :
#    반복 수행 문장 ;

count =1;
total= 0;
while count <=10:
    print(count);
    total = total + count;
    print(total);
    count = count + 1; #자바에서는 i++ 연산자 형태로 썼음. 

'''
##실습 
mynum = 50;
while True :

키보드 입력: 50 보다 크면 작은 숫자를 생각해보세요 출력
                 50 보다 작으면 큰 숫자를 생각해보세요 출력
                  50이면 맞췄습니다 출력 - 반복 종료 (break ;)
    yournum = int(input()) #문자열에서 정수타입으로 변경 
    if yournum > 50 :
        print("작은 숫자를 생각해보세요") ;
    elif yournum < 50 :
        print("큰 숫자를 생각해보세요") ;
    else : 
        print("맞췄습니다");
    break ;
'''
'''
#내가 작성한 코드 
mynum = 50;
count = 0; 
while True :    
    print(count);
    total = total + count;
    print(total);
    count = count + 1;

    if count > mynum :
        print("작은 숫자를 생각해보세요") ;
    elif  count < mynum :
        print("큰 숫자를 생각해보세요") ;
    else
        print("맞췄습니다");
    break ;
'''


##실습 

lottoset = set();
#데이터 없는 set 생성 함수 - ()
#중복 데이터 미허용. add 무시 
'''
lettoset 에 1-45 번호 (random randint(1, 45)) 6개 생성 저장
while 반복문
set변수.add(), let(set변수)
'''
import random
lottoset =set();
cnt = 0;
while True:
    lotto = random.randrange(1,46);
    cnt = cnt +1;
    print(lotto);
    print("{}번째 난수 {}를 생성합니다".format(cnt, lotto));
    lottoset.add(lotto) ;
    if len(lottoset) == 6 :
        break ;


#for 변수 in 반복횟수 :
#    반복 수행 문장 ;

    
print(range(1, 11, 1)); # 1 2 3 ... 10
#1부터 시작 10까지의 범위 1씩 증가

for i in range(5, 51, 10) :
    print(i);


for i in range(11) :
    print(i);



a = [1,2,3,4,5]
print(a); #[1,2,3,4,5]

for i in a:
    print(i);


for i in range(0, len(a), 1):
    print("{}번째 인덱스값은 {}입니다".format(i, a[i] ));

for i in [1,2,3,4,5] :
    print(i);

for i in [1,2,3,4,5] :
    print(i);

d = {"k1":1, "k2": 2, "k3": 3, "k4": 4, "k5": 5};

#(1, 2) - tuple
#a, b = (1,2)

# ("k1":1, "k3":3 )
#d.items()

for key, value in d.items():
    print("{}키의 값은 {}입니다".format(key, value));






'''
#파이썬 기본 내장 함수
print("math.abs(-10)=", abs(-10))
print("math.round(a/b)=", round(a/b))

#파이썬 기본 내장 함수 확인 
print(dir(__builtins__))
print(dir(a)) #str 타입 포함 함수 목록 확인
'''


'''
#파이썬 사용자 정의 함수
# 자바스크립트 함수/ 메소드 = 파이썬 함수/메소드 = 자바 메소드 
# 함수 - 입력값(매개변수), 특정 기능 구현 문장 - 결과 리턴값

#정의 메모리 할당 x 
def 함수이름(매개변수) :
    들여쓰기 문장:
    들여쓰기 문장:
    return 값:

#호출 실행 메모리 할당 o 
리턴결과변수 = 함수이름(값 전달)



abs()
d.tiems()
'''




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
    for i in range(1, n+1, 1):
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

