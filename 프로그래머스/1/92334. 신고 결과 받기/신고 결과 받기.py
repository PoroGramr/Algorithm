"""
문제 이해하기
- 입력
    - id_list : 유저의 목록 [리스트]
    - report : 유저가 신고한 목록 [리스트] "신고한 사람 신고당한 사람"
    - k : 정지 기준이 되는 신고 횟수
- 출력
    - 신고가 모두 끝난 후 유저가 받게되는 정지 안내 메일 수 [리스트]
    - 한 사람이 여러명을 신고할 수 있음
    - 한 사람이 한명을 여러번 신고할 수는 없음(중복 불가))
    - 신고가 모두 완료된 후에 정지 메일을 받음

아이디어
- 신고 받은 사람의 신고 횟수
- repoter가 신고한 사람중에 정지당한 사람의 수를 세기

제한 사항
-id_list :n: 1000 1k
- report : 200,000 200k
- O(n*m) 1k * 200k = 200M

"""

def solution(id_list, report, k):
    answer = []
    # reportTable: 신고 당한 사람을 누가 신고했는지 dict
    reportTable = {}
    for id in id_list:
        reportTable[id] = []
    
    # 신고 당한 사람이 unique하게 몇번 신고당했는지 확인
    # reportTable 채우기
    for rep in set(report):
        reporter, reported = rep.split()
        reportTable[reported].append(reporter)

    
    # bannedTable: 유저리스트 -> 누가 정지했는지 확인하는 테이블
    bannedTable = {}
    for id in id_list:
        #  - k랑 비교
        if len(reportTable[id]) >= k:
            bannedTable[id] = True
        else:
            bannedTable[id] = False

    
    # id_list를 기준으로 내가 신고한 사람중에 몇명이나 정지했는지 확인
    mailCntTable = {}
    for id in id_list:
        mailCntTable[id] = 0
    
    for reported, repoters in reportTable.items():
        if bannedTable[reported]:
            for rep in repoters:
                mailCntTable[rep] += 1

    for id in id_list:
        answer.append(mailCntTable[id])
    return answer