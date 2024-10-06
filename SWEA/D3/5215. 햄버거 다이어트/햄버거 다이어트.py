
def dfs(ii, sumc, curt): # index of ingredint, sum of calrorie , curent taste
    global maxTaste
    
    if ii == N:
        if sumc <= L:
            maxTaste = max(curt, maxTaste)
        return

    

    # 만약 해당 재료를 추가한다면
    dfs(ii+1,sumc + data[ii][1], curt + data[ii][0])

    # 추가하지 않는다면
    dfs(ii+1, sumc,curt)


T = int(input())

for i in range(1, T+1):
    N, L = map(int, input().split()) # N : count of ingredient. L : calorie limit
    data = []
    for _ in range(N):
        ing, cal = map(int, input().split()) # ingredient, calorie
        data.append([ing,cal])
    maxTaste = 0
    dfs(0,0,0) # index of ingredint, sum of calrorie , curent taste
   
    print(f"#{i} {maxTaste}")



