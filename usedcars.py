#usedcards.csv

#마일리지가 20000 이상이면 "폐차 직전"
#10000 이상 ~ 20000 미만 "심각한 중고"
#10000 미만이면 "양호한 중고"
'''
출력 값의 형태가 
2011	SEL	21992	7413	Yellow	AUTO "양호한 중고"
'''
#import sys
#sys.getcwd()


#그래프에 넣기 위해 수정
file = open("usedcars.csv", "r")
total = 0

car_state = []
car_state_values = ["폐차 직전", "심각한 중고", "양호한 중고"]
car_state_cnt = [] #갯수

#file.read() #파일 모든 문자열 리턴
for line in file : #라인 수만큼 반복
    total = total +1 
    line_list = line.split(",") #str
    #print(line_list)
#list = [year,	model,	price,	mileage, color,	transmission]

    #list[] = str 타입 
    #year = line_list[0]
    #model = line_list[1]
    #price = line_list[2]
    mile = line_list[3]
    #color = line_list[4]
    #trans = line_list[5]
    if mile.isdigit() and int(mile) >= 20000 :
        line_list.append(car_state_values[0]); 
    elif mile.isdigit() and int(mile) >= 10000 and int(mile) < 20000 :
        line_list.append(car_state_values[1]);
    elif mile.isdigit() and int(mile) < 10000 :
        line_list.append(car_state_values[2]);
    else :
        line_list.append("차량 상태");
    print(line_list)
    car_state.append(line_list[6]);

'''
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
'''
file.close()
print("총 차량 댓수=", total);


for car_val in car_state_values :
    car_state_cnt.append(car_state.count(car_val))

import matplotlib.pyplot as plt
plt.rcParams['font.family'] = "Batang"
plt.title("중고차 상태")
#plt.plot(car_state_values, car_state_cnt)
plt.hist(car_state[1: ]) #x축 (150개) y축 자동으로 빈도 수 
plt.show()


#각 항목별 갯수 확인 => car_stae_cnt
#print(car_state.count("폐차 직전"))
#print(car_state.count("심각한 중고"))
#print(car_state.count("양호한 중고"))



