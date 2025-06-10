'''
같은 시간대에 게임을 이용하는 사람이 m명 늘어날때 마다 서버 1대가 추가로 필요
어느 시간대의 이용자가 m명 미만이라면 서버 증설이 필요하지 않음

어느 시간대의 이용자가 n*m 이랑 (n + 1) * m 명 미만이라면 최소 n대의 증설된 서버가 운영 중이어야 함
한 번 증설한 서버는 k 시간 동안 운영하고 그 이후에는 반납, k = 5 일때 10시에 증설했다면 10 ~ 15시 동안 운영
'''

def solution(players, m, k):
    # m 명 늘어날 때 마다 서버 증설, k시간동안 서버 운영
    server = [0 for _ in range(24)]
    
    # 서버 증설 후 삭제되어야 하는 시간
    serverDelete = []
    
    # 현재 서버 수
    currentServer = 1
    
    count = 0
    for i in range(24):

        print("현재 시간", i,"이용자",players[i],"서버 수", currentServer)
        # print(serverDelete)
        
        for d in range(len(serverDelete)):
            if serverDelete[d] == i:
                currentServer -= 1
                
        if players[i] >= currentServer * m:
            blockPlayers = players[i] - currentServer * m
            addServer = blockPlayers // m + 1
            currentServer += addServer
            count += addServer
            
            for _ in range(addServer):
                serverDelete.append(i + k)
                
    return count