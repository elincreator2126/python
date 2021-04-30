#웹 크롤링 기상청 정보 + 그래프
#데이터 가져와서 - 전처리 - 데이블, 그래프 - 분석 - 결과 테이블, 그래프 (시각화)

#그래프 방법
#pip3 install matplotlib 설치

import matplotlib.pyplot as plt

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10] #반드시 리스트 아니어도 됨 

import random
c= []
for i in range(1, 11, 1):
    c.append(random.randint(1, 10))

''' 1번에 1개 
#plt.plot(a, b, "o") #점 
#plt.plot(a, b) #선
#두 데이터의 개수가 같으면 됨
plt.title("graph")
plt.xlabel("a")
plt.ylabel("b")
plt.savefig("test.png")

plt.show()

print(c)
plt.hist(c) #히스토그램
plt.show()
'''
'''
plt.subplots()
plt.plot(a,b)
plt.plot(b,a, 'o')
plt.hist(c)
plt.savefig("test.png")
plt.show()
'''

plt.subplot(2, 2, 1)
plt.plot(a,b)

plt.subplot(2, 2, 2)
plt.plot(a,b, 'o')

plt.subplot(2, 2, 3)
plt.hist(c)

plt.show()


#
#import urllib.request as req
#pip install beautifulsoup
#}import bs4.BeautifulSoup as bs

#pip3 install requests
import requests #install 후 가능 

#get
#response = requests.get("http://127.0.0.1:9090/?id=aaa&pw=1234").text()



#post
#test.png 파일 업로드
graphfile = open("test.png", "rb")
#현재경로에서의 파일이면 파일명만 
#그림은 byte 처리 => "rb"로 표현 
response = requests.post("http://127.0.0.1:9091/fileupload",
                         data={"name": "python", "description":"fileupload"},
                         files={"file1": graphfile, "file2": graphfile})
                    #{} set(데이터 나열), dict(키와 값이 한 쌍으로)

#전송자 <input type=text name="name" value="전송하는사람"> <br>
#설명 <input type=text name="description" value="파일 설명"> <br>
#파일명1: <input type="file" name="file1"><br>
#파일명2:<input type="file" name="file2"> <br>

print(response.status_code) #200 
print(response.text) #@ResponseBody 잘 받았습니다. 문자열 응답 #uploadresult.jsp 응답           


#웹 크롤링 기상청 정보 + 그래프 + 파일 저장 + spring 파일 업로드 구현
#spring 파일 업로드 구현
#파라미터 4개






                         
