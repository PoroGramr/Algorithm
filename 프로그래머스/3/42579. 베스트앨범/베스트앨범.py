def solution(genres, plays):
    genreDict = {}
    
    answer = []
    #1. 많이 재생된 장르 추출
    for i in range(len(genres)):
        genreDict[genres[i]] = genreDict.get(genres[i], 0) + plays[i]
    
    sortedDict = sorted(genreDict.items(), key = lambda x : -x[1] )
    
    print(sortedDict)
    
    #2. 장르 내에서 많이 재생된 노래 추출(고유 번호 : 재생된 수)
    for a in range(len(sortedDict)):
        popular = {}
        for j in range(len(genres)):
            if genres[j] == sortedDict[a][0]:
                popular[j] = plays[j]
        
        print(popular)
        sortedPopular = sorted(popular.items(), key = lambda x : -x[1])
        print(sortedPopular)
        if (len(sortedPopular)) == 1:
            answer.append(sortedPopular[0][0])
        else:
            for k in range(2):
                answer.append(sortedPopular[k][0])
    #3. 재생횟수가 같다면 고유 번호가 낮은 노래를 먼저 추출

    return answer