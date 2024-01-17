#백준 2720

n = int(input())
for _ in range(n):            # 테스트 케이스 개수
	money = int(input())
	for i in [25, 10, 5, 1]:
		print(money//i, end=' ')  # //은 나눗셈의 몫 5 // 3 = 1
		money = money%i           # %은 나눗셈의 나머지 5 % 3 = 2
