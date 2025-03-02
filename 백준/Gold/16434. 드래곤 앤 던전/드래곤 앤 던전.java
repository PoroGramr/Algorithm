import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");

        // 방의 개수
        int roomCount = Integer.parseInt(input[0]);
        // a용사의 초기 공격력
        long basicAd = Integer.parseInt(input[1]);

        // 방 정보 배열
        int[][] roomsInfo = new int[roomCount][3];

        for(int i = 0; i < roomCount; i++){
            String[] roomData = br.readLine().split(" ");
            roomsInfo[i][0] = Integer.parseInt(roomData[0]);
            roomsInfo[i][1] = Integer.parseInt(roomData[1]);
            roomsInfo[i][2] = Integer.parseInt(roomData[2]);
        }

        // 이분 탐색 범위 설정
        long left = 1;
        long right = Long.MAX_VALUE / 2; // 충분히 큰 값 (오버플로우 방지)
        long answer = right;

        while(left <= right){
            long mid = left + (right - left) / 2; // 오버플로우 방지
            
            // mid 값이 충분한 최대 체력인지 확인
            if(canClearDungeon(mid, basicAd, roomCount, roomsInfo)){
                answer = mid;
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }

        System.out.println(answer);
    }

    // 특정 최대 체력으로 던전을 클리어할 수 있는지 확인하는 메서드
    public static boolean canClearDungeon(long maxHp, long basicAd, int roomCount, int[][] roomsInfo){
        long currentHp = maxHp; // 시작 체력은 최대 체력
        long currentAd = basicAd; // 현재 공격력
        
        for(int i = 0; i < roomCount; i++){
            // 몬스터가 있는 방
            if(roomsInfo[i][0] == 1){
                long monsterHp = roomsInfo[i][2];
                long monsterAd = roomsInfo[i][1];
                
                // 몬스터를 처치하기 위해 필요한 공격 횟수 (올림)
                long attackCount = (monsterHp + currentAd - 1) / currentAd;
                
                // 용사가 받는 데미지 (마지막 턴에는 몬스터가 공격하지 않음)
                long damageTaken = monsterAd * (attackCount - 1);
                
                // 용사의 현재 체력에서 데미지 차감
                currentHp -= damageTaken;
                
                // 체력이 0 이하면 던전 클리어 실패
                if(currentHp <= 0){
                    return false;
                }
            } 
            // 포션이 있는 방
            else if(roomsInfo[i][0] == 2){
                currentAd += roomsInfo[i][1]; // 공격력 증가
                currentHp += roomsInfo[i][2]; // 체력 회복
                
                // 회복된 체력이 최대 체력을 초과하면 최대 체력으로 제한
                if(currentHp > maxHp){
                    currentHp = maxHp;
                }
            }
        }
        
        // 모든 방을 통과했으면 던전 클리어 성공
        return true;
    }
}
