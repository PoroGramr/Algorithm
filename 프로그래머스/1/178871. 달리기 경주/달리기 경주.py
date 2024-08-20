"""
문제 이해
 - 입력 : 선수들의 이름이 담긴 players 리스트, 해설진의 추월 알림이 담긴 callings 리스트
 - 출력 : 선수들의 순위 결과 리스트

제한사항
 - n : 50,000 -> 50k
 - m : 1,000,000 -> 1M
 - O(n*m) 50k * 1M -> 50G

아이디어
 - calling을 순회하며 불려진 선수를 찾아 players 리스트의 순서를 바꿔준다.
"""
def solution(players, callings):
    
    # - rank 딕셔너리 만들기 {플레이어 이름 : 인덱스}
    ranks = {}
    for idx, player in enumerate(players):
        ranks[player] = idx
    
    
    # - calling 만큼 반곳
    for call in callings:
        curRank = ranks[call]
        tarRank = curRank - 1
        tarPlayer = players[tarRank]
        
        players[curRank],players[tarRank] = players[tarRank],players[curRank] 
        
        ranks[call] = tarRank
        ranks[tarPlayer] = curRank
    #   - rank[player] : 선수의 순위를 찾기
    #   - 선수의 순위를 앞선 선수랑 바꾸기 : players
    #   - 바뀐 순위를 rank에 업데이트 해주기

    return players