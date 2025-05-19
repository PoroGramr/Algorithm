def solution(genres, plays):
    # 1. 장르별 총 재생 횟수 계산
    genre_play_sum = {}
    for g, p in zip(genres, plays):
        genre_play_sum[g] = genre_play_sum.get(g, 0) + p

    # 2. 장르별 곡 리스트 생성
    songs_by_genre = {}
    for idx, (g, p) in enumerate(zip(genres, plays)):
        songs_by_genre.setdefault(g, []).append((idx, p))

    # 3. 장르별 곡을 재생 수 내림차순, 인덱스 오름차순으로 정렬
    for g in songs_by_genre:
        songs_by_genre[g].sort(key=lambda x: (-x[1], x[0]))

    # 4. 장르를 총 재생 횟수 내림차순으로 정렬
    sorted_genres = sorted(genre_play_sum.keys(),
                           key=lambda g: genre_play_sum[g],
                           reverse=True)

    # 5. 각 장르에서 상위 2곡씩 추출하여 답안 리스트 작성
    answer = []
    for g in sorted_genres:
        top_two = songs_by_genre[g][:2]
        for idx, _ in top_two:
            answer.append(idx)

    return answer