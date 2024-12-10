score = { "A+" : 4.5, "A0" : 4.0, "B+" : 3.5, "B0" : 3.0, "C+" : 2.5, "C0" : 2.0, "D+":1.5, "D0" : 1.0, "F" : 0.0} 


allBook = 0

allScore = 0


for _ in range(20):
    inData = list(map(str, input().split()))
    if inData[2] == "P":
        continue
    else:
        allBook += float(inData[1])
        allScore += score[inData[2]] * float(inData[1])

answer = allScore / allBook 
print(answer)

