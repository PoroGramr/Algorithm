T = 10
for t in range(1, T+1):
	N = int(input())
	data = list(map(int, input().split()))
	ans = 0

	for i in range(2, N - 2):
		left1 = data[i-2]
		left2 = data[i-1]
		right1 = data[i+1]
		right2 = data[i+2]

		if left1 < data[i] and left2 < data[i] and right1 < data[i] and right2 < data[i]:
			ans += data[i] - max(left1, left2, right2, right1)	
    
	print(f"#{t} {ans}")