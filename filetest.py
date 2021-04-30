# 파이썬 데이터 소스(웹사이트, 파일)로부터 데이터 가져와서 분석 - 결과 테이블, 그래프
# 파일 입출력 간단
#파일 읽기
import os
print(os.getcwd()) #파이썬 저장경로 C:\kdigital\python_source
print(os.listdir())
#목록 ['.git', 'basic.py', 'exceptiontest.py', 'filetest.py', 'moduletest.py', 'pip install beautiful4.png', 'second.py']

try : 
    file = open("moduletest.py", "r", encoding="utf-8" ) #r | w | a | b
    print(file.read()) #UnicodeDecodeError => 한글 읽기를 하지 못했다.
    #"str" , 각 라인 옆 번호 생성은 어려움
except FileNotFoundError:
    print("a. txt 파일 없어요")
file.close();


#파일 없으면 새로 생성 (w)
file2 = open("a.txt", "w") 
file2.write("새로운 파일을 생성합니다.");
file2.close() 

#파일 있으면 기존 내용 뒤에 추가 쓰기 저장 (a)
file2 = open("a.txt", "a") 
file2.write("Wn새로운 라인을 추가합니다.Wn");
file2.close()

#파일 한 라인씩 읽어서 리스트에 저장 (r)
#file_list = []
file_list = list()
file3 = open("moduletest.py", "r", encoding="UTF-8")
for line in file3:
    file_list.append(line);
file3.close();


'''
#리스트에 저장 내용 화면 출력 
linenum = 1; 
for line in file_list:
    print(linenum, " 번 라인 : ", line, end="Wn " );
    linenum = linenum +1;
'''


#리스트에 저장 내용 화면 출력
for index in range(0, len(file_list), 1):
    print(index+1 , " 번 라인: ", file_list[index], end=" ");
    

#print(*val, sep=" ", end="Wn"
#1번 라인: xxx
#2번 라인: xxxx



#라인 번호 있는 상태의 모든 내용을 파일 copy.txt에 저장
file4 = open("copy.txt", "w");

for index in range(0, len(file_list), 1):
    line = str(index + 1) + " 번 라인 : "  + file_list[index];
    file4.write(line);

file4.close(); #탐색기에서 copy4.txt 파일 이름 변경 - 다른 프로그램 사용 중..



#usedcards.csv

#마일리지가 20000 이상이면 "폐차 직전"
#10000 이상 ~ 20000 미만 "심각한 중고"
#10000 미만이면 "양호한 중고"
'''
출력 값의 형태가 
2011	SEL	21992	7413	Yellow	AUTO "양호한 중고"


'''

'''내가 작성한 코드 - 잘못
#r w a b 
usedcars_list = list()
usedcars_file = open("usedcars.csv", "r", encoding="UTF-8")

for line in usedcars_file :
    usedcars_list.append(list[7]) =status ;
    for index in range(0, len(file_list), 1):
    line = str(index + 1) + " 번 라인 : "  + usedcars_list[index];

list = [year,	model,	price,	mileage, color,	transmission]
list.append = "status"
#[year,	model,	price,	mileage, color,	transmission, status] 
    if list[4] > = 20000 :
        print(list + list[7] + "폐차 직전" );
    elif list[4] > = 1000 & list[4] < 20000 :
        print(list + list[7] + "심각한 중고" );
    else :
        print(list + list[7] + "양호한 중고" );
    
usedcars_file.close();
'''





