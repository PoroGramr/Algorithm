def solution(absolutes, signs):
    answer = 0
    # for i in range(len(absolutes)):
    #     if signs[i] == True:
    #         answer += absolutes[i]
    #     else:
    #         answer -= absolutes[i]
            
    for value, sig in zip(absolutes, signs):
        if sig:
            answer += value
        else:
            answer -= value
    return answer