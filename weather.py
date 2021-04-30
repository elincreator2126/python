#접속해서 모든 태그 출력


import urllib.request as req
from bs4 import BeautifulSoup as bs


response = req.urlopen("http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108")
soup = bs(response, "html.parser")
#print(soup.prettify())


#서울 날씨, 최고기온, 최저기온 (1일마다 2개씩, 1주일)
#지역이름 출력
'''
#잘못된 코딩의 예 -> 도시는 다 다른데, wf내용이 같음 
city_list = soup.select("city");
wf = soup.select_one("wf");
print(len(city_list))

for city in city_list :
    print();
    wf = soup.select_one("wf")
    print(city.string + ":" + wf.string);
    #.string => 태그들 제외하고 데이터만 가져옴     
'''

#참고
'''
<location wl_ver="3">
<province>서울ㆍ인천ㆍ경기도</province>
<city>서울</city>
<data>
1일차 00시
<mode>A02</mode>
<tmEf>2021-05-03 00:00</tmEf>
<wf>맑음</wf> 날씨
<tmn>10</tmn> 최고기온
<tmx>20</tmx> 최저기온 
<reliability/>
<rnSt>0</rnSt>
</data>
<data>
1일차 12시
<wf>맑음</wf> 날씨
<tmn>10</tmn> 최고기온
<tmx>20</tmx> 최저기온 
<reliability/>
<rnSt>0</rnSt>
</data>
</location> 
'''
print(len(soup.select("location")));

city_list = []
tmx_list = []
tmn_list = []
for loc in soup.select("location"): #41번 str
    #location 태그 안에서 해당 사항을 찾으라는 의미
    
    print("----------------------------------------")
    print("도시:",  loc.select_one("city").string);
    print("시간:",  loc.select_one("tmEf").string);
    print("날씨상황:",  loc.select_one("wf").string);
    print("최고기온 :",  loc.select_one("tmn").string);
    print("최저기온 :",  loc.select_one("tmx").string);
    print("----------------------------------------")
    
    city_list.append(loc.select_one("city").string)
    tmx_list.append(loc.select_one("tmx").string)
    tmn_list.append(loc.select_one("tmn").string)


tmx_list = list(map(int, tmx_list ) )
tmn_list = list(map(int, tmn_list ) )


#그래프 설정 
#한글도 출력하는 폰트 - 궁서체 굴림체 바탕체 돋움체
#컴퓨터 설치 사용 글꼴 정보
'''
import matplotlib.font_manager as fm

fname_list = []
for f in fm.fontManager.ttflist : 
    fname_list.append(f.name) ;
    #print(f.name)
'''


#fname_list.sort() #sort는 리턴값 없음 
#for name in fname_list:
    #print(name)


#x축 도시명 y축 최고기온 그래프
import matplotlib.pyplot as plt

#글꼴 세팅
plt.rcParams["font.family"] = "Batang" ;
plt.rcParams["font.size"] = 15 ;
plt.rcParams["figure.figsize"] = (12, 6) ;

plt.rcParams["xtick.labelsize"] = 8; #x축 데이터 글씨 크기 (서울 인천 제주 ..)
plt.rcParams["axes.labelsize"] = 10; #x축 레이블 글씨 크기 
plt.rcParams["lines.linewidth"] = 3;
plt.rcParams["lines.linestyle"] = '-.' #그래프 선 모양 
plt.rcParams["axes.grid"] =True #그래프 그리드 표시 

plt.plot(city_list, tmx_list) #x축 순서 y 
plt.title('도시별 최고기온')
plt.xlabel("도시명")
plt.ylabel("max")
plt.show()

#1개 그래프(축 공유)에 도시별 최고기온과 최저기온 동시에 표현 

plt.subplots()
plt.plot(city_list, tmx_list)
plt.plot(city_list, tmn_list)
plt.savefig("weather.png")
plt.show();


#실습
'''
usedcars.csv 파일 읽어서
mile: "폐차 직전" , "심각한 중고", "양호한 중고"
    
1> 각 해당 항목의 마일리지 개수 확인
2> 그래프 x축 레이블 = 상태, y축 레이블 = 차량댓수
    x축 데이터 = ['폐차직전' ...]
    y축 데이터 = ...
'''
#데이터 파일 

file3 = open("usedcars.py", "r", encoding="UTF-8")
import matplotlib.pyplot as plt2
mile_list = []
number_list = []

plt2.plot(mile_list, number_list) #x축 순서 y 
plt2.title('마일리지별 중고차 상태')
plt2.xlabel("상태")
plt2.ylabel("차량댓수")
plt2.show()



'''
#데이터 코드 
file = open("usedcars.csv", "r")
total = 0 
#file.read() #파일 모든 문자열 리턴
for line in file : #라인 수만큼 반복
    total = total +1 
    line_list = line.split(",") #str
    print(line_list)
#list = [year,	model,	price,	mileage, color,	transmission]


    #list[] = str 타입 
    year = line_list[0]
    model = line_list[1]
    price = line_list[2]
    mile = line_list[3]
    color = line_list[4]
    trans = line_list[5]
    if mile.isdigit() and int(mile) >= 20000 :
        line_list.append("폐차 직전"); 
    elif mile.isdigit() and int(mile) >= 10000 and int(mile) < 20000 :
        line_list.append("심각한 중고");
    elif mile.isdigit() and int(mile) < 10000 :
        line_list.append("양호한 중고");
    else :
        line_list.append("차량 상태");
    print(line_list)

print("총 차량 댓수=", total);
file.close()
'''

