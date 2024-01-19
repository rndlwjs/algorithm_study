#그리디 알고리즘: 현재 시점에 가장 좋은 선택
	#그리디는 기타 알고리즘에 비해 빠른 장점이 있다. 하지만 다음과 같은 특징에서만 사용될 수 있다.
	#특징1: 현재 선택이 미래의 선택에 영향을 끼치지 않을 때
	#특징2: 부분의 최적 해가 모이면 전체의 최적 해가 될때
	#예시) 서울 - 대전 - 부산 경로에서, 서울과 대전의 거리는 대전과 부산 경로에 영향을 미치지 않는다. 서울 대전의 최단 거리를 구하고, 대전 부산 최단 거리를 구하는 것이 전체 길이의 최단 길이를 구하는 것이다.

###백준 세탁소 사장 동혁 (2720)

n = int(input())
for _ in range(n):            # 테스트 케이스 개수
	money = int(input())
	for i in [25, 10, 5, 1]:
		print(money//i, end=' ')  # //은 나눗셈의 몫 5 // 3 = 1
		money = money%i           # %은 나눗셈의 나머지 5 % 3 = 2

###백준 전자레인지 (10162)

time = int(input())
for i in [300, 60, 10]:
    if time % 10 != 0:
        print(-1)
        break			#서브태스크 만족시키는 조건
    else:
        print(time // i, end=" ")
        time = time % i

###백준 거스름돈 (5585)

money = 1000 - int(input())
result = 0
for i in [500, 100, 50, 10, 5, 1]:
    result = result + money // i
    money = money % i
print(result)

###백준 캠핑 (4796)
index = 0

while True:
    index += 1
    L, P, V = map(int, input().split())
    if L==0 and P==0 and V==0:
        break
    times   = V // P    #횟수
    left    = V % P     #남은 시간
    if L < left:        #중요한 부분!! 큰걸 먼저 처리하고, 다음으로 작은걸 처리한다
        left = L        #최적의 해를 구하기 위한 과정 (캠핑을 더 갈 수 있으면, 더 가는 것이 최적의 해)
    days = L * times + left
    print("Case %d: %d" %(index, days))

###백준 설탕배달 (2839)
#허용해야 되는 케이스
#3의 배수 6, 9, 12, (15)
#3의 배수 + 5의 배수인 경우 11,(14),17,31
#작은 것을 먼저 제거하고, 큰 것을 택하는 방법

num     = int(input())
n_bag   = 0

while num >= 0:
    if num % 5 == 0:
        print(n_bag + num//5)
        break
    num -= 3    #만약 여기서 0보다 작아지면, while 조건 탈출하기 때문에, num>=0으로 설정해야 한다.
    n_bag += 1

    #if num % 5 == 0: #num>0으로 하면 한번 더 실행 해야한다.
    #    print(n_bag + num//5)
    #    break

else: print(-1) #while-else 사용해도 된다
