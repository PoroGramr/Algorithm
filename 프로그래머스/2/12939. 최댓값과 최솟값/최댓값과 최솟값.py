def solution(s):
    data = list(s.split(" "))
    for i in range(len(data)):
        data[i] = int(data[i])
    answer = (str(min(data))+" "+str(max(data)))
    return answer 