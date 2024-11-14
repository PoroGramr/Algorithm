T = int(input())
alphabet = list(map(str, "abcdefghijklmnopqrstuvwxyz"))

for t in range(1, T + 1):
    IN = list(map(str, input()))
    
    count = 0
    
    for i in range(len(IN)):
        if alphabet[i] == IN[i]:
            count +=1
        else:
            break
    
    print(f"#{t} {count}")
