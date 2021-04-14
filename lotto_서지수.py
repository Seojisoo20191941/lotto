import random

#로또 총 장수 출력하기
def printpaper(money):
    paper=int(money/1000)
    return paper
    
#랜덤 생성된 로또 출력하기
def randomlotto(paper):
    all_list=[]
    for n in range(paper):
        list=[]
        num=random.randint(1,45)
        for i in range(6):
            while num in list:
                num=random.randint(1,45)
            list.append(num)
        list.sort()
        all_list.append(list)
    
    return all_list

#지난 주 당첨 번호를 입력 받기
def lastlotto(): 
    last_num=input(">지난주 당첨 번호를 입력해주세요")
    last_num=last_num.split(',')
    for i in range(len(last_num)):
        last_num[i]=int(last_num[i])
    return last_num

#로또 당첨 결과 출력하기
def result(all_list, last_num):
    fourth=0
    third=0
    second=0
    first=0
    for i in range(paper):
        correct=0 #맞은 번호 수
        for j in range(6):
            if all_list[i][j]==last_num[j]:
                correct+=1
        if correct==6:
            first+=1
        elif correct==5:
            second+=1
        elif correct==4:
            third+=1
        elif correct==3:
            fourth+=1

    return fourth, third, second, first

    
#수익률 출력하기
def resulty(fourth, third, second, first):
    total=fourth*5000+third*20000+second*100000+first*5000000
    y=total/money #수익률
    return y

#def main():
#구입금액 입력받기
while True:
    money=input(">구입금액을 입력해 주세요.")
    if money.isalpha():
        print('숫자를 입력해주세요') #문자열 입력시
    else:
        money=int(money)
        if money==0:
            print('로또의 최소 가격은 1000원입니다')
        else:
            break
        

paper=printpaper(money)
print(">%d장의 로또를 구입하셨습니다." %paper)
    
all_list=randomlotto(paper)#뽑은 로또 
for i in range(len(all_list)):
    print(all_list[i])
    
while True:#지난주 로또 번호가 6자리인지 확인 후 예외처리
    last_num=lastlotto()
    if len(last_num)==6:
        break
    else:
        print('로또는 6개의 숫자로 이루어집니다.')

fourth, third, second, first=result(all_list, last_num)
print(">로또 당첨 결과")
print("4등(3개가 맞을 때) - 5000원 - %d개" %fourth)
print("3등(4개가 맞을 때) - 20000원 - %d개" %third)
print("2등(5개가 맞을 때) - 100000원 - %d개" %second)
print("1등(6개가 맞을 때) - 5000000원 - %d개" %first)

y=resulty(fourth, third, second, first)
print('>수익률\n%.2d배' %y)


