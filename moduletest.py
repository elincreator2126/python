#module = 물리적 = *.py
# 파이썬 라이브러리 -1 회사 / 단체 관리 z - pypi.org - 라이브러리 다운로드
'''
#이미 설치 몇 개 모듈 사용
import random
import math
import time
import sys

random.randint(1,10)
math.trunc(3.14)
time.sleep(5)
print(sys.argv[1])
'''

#다른 모듈 import 1
import math 
math.trunc(3.14)
math.log(10,2)



#다른 모듈 import 2
from math import trunc, log 
trunc(3.14)
log(10, 2)


#다른 모듈 import 3
from math import * 
trunc(3.14)
log(10, 2)



#다른 모듈 import 4
import math as ma
ma.trunc(3.14)
ma.log(10,2)




import random
print(random.randint(1,100))
print(random.randrange(1,101))
name_list = [ "abcde", "가나다라", "ab가나", "xyz"] 
print(random.choice(name_list))
random.shuffle(name_list)
print(name_list)
print(random.sample(name_list, 2))


import sys
#print(sys.argv[1])
print(sys.version)
print(sys.getwindowsversion())
print(sys.path) #내장모듈 + 사용자모듈 + 외부설치추가모듈 저장경로

import os
print(os.name)
print(os.getcwd())
print(os.listdir())

import datetime
now = datetime.datetime.now()
print(now.year) 
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)

after_1year = now.replace(year = (now.year +1));
print("1년뒤=", after_1year.year);




import time
sec = time.time() #현재시간을 초단위
now = time.localtime(sec) #년월일시분초 변경 
print(now.tm_year)


#아직 설치되지 않은 모듈 설치 - import - 사용코드
#자바 라이브러리 - ojdbc6.jar(오라클 폴더 -> jre..) jst1.jar
# 도스 pip (python install pakage)

#명령 프롬프트 (dos) 
#pypi.org 사이트 검색 - 명령어 복사
#pip install beautifulsoup4
#pip list
#pip show beautifulsoup4 - location 정보 
#sys.path 포함 


import urllib.request as req #웹서버에 접속 urlib 

from bs4 import BeautifulSoup as bs

response = req.urlopen("http://127.0.0.1:9091/");
soup = bs(response, "html.parser");

#전체 내용 출력 
rescontents = soup.prettify();
#rescontents = response.read();
print(rescontents);

#h3 태그
print(soup.find("h3")); #type : dict  string: xxx, style: xxx
print(soup.find("h3").string);
print(soup.find("img")['src']);
for h3 in soup.findAll("h3"): 
    print(h3.string)
response.close();


for i in range(1, 11, 1): #문법검사 + 실행 
    print(i);

#자바 c c++ c# --> 컴파일 언어
#    자바소스 파일 -> 1~ 마지막까지 문법 검사 = 바이너리 코드로 변경(컴파일 결과 저장 .class파일 - 실행  
#자바스크립트 파이썬 --> 1문장마다 문법 검사, 실행  인터프리터 언어


#print(a) #문법검사가 하는 건 잘못된 문법만 없나 를 검사
#a가 있는지 없는지는 실행을 해봐야 알아.
#NameError : name 'a' is not defined 





































