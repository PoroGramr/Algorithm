grade = ["A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"]

T = int(input())

for t in range(1, T+1):
    N, K = map(int, input().split())  # 학생 수, 학점을 알고 싶은 학생의 번호

    scores = []
    for i in range(N):
        mid, final, hw = map(int, input().split())  # 중간고사 점수, 기말고사 점수, 과제 점수
        total_score = mid * 0.35 + final * 0.45 + hw * 0.2
        scores.append([total_score, i])  # 점수와 학생 번호를 함께 저장

    # 점수가 높은 순서대로 정렬
    scores.sort(key=lambda x: -x[0])

    # 학점을 알고 싶은 학생의 순위 계산
    for idx in range(len(scores)):
        if scores[idx][1] == K - 1:  # K번 학생의 실제 인덱스는 K-1이므로
            rank = idx

    # 전체 학생을 10개의 구간으로 나누기
    findRankSolid = N // 10

    # 해당 순위에 맞는 학점을 부여
    ans = grade[rank // findRankSolid]

    print(f"#{t} {ans}")
