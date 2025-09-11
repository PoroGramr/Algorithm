def solution(word):
    data = ["A", "E", "I", "O", "U"]
    dic = []

    for a in data:
        s1 = a
        dic.append(s1)
        for b in data:
            s2 = s1 + b
            dic.append(s2)
            for c in data:
                s3 = s2 + c
                dic.append(s3)
                for d in data:
                    s4 = s3 + d
                    dic.append(s4)
                    for e in data:
                        s5 = s4 + e
                        dic.append(s5)

    return dic.index(word) + 1