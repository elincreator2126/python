
'''
try:
    print(a)
except NameError :  #ValueError  실행되지 않아. 
    print("a 변수 선언된 적이 없어요")
'''

try :
    money = input("대출금액 상환개월 수 입력하세요 : " );
    #"1000 12".split()
    two_items = money.split();
    loan = int(two_items[0]);
    payback = int(two_items[1]);
    if payback <= 0 :
        raise ValueError("상환 개월은 음수 값을 입력할 수 없습니다.") 
    monthly_return = loan / payback;
except IndexError :
    print("대출 금액이나 개월 수 입력 확인하세요 ")
except ValueError as ve :
    print(ve); #invalid literal for int() with base 10:
    #print("대출 금액이나 개월 수 정수로만  입력하세요 ")
else : #오류없이 정상 실행되었을 때 
    print(monthly_return ," 을 매달 상환하셔야 합니다.")
finally:
    print("영업 종료");
