import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        List<int[]> times = new ArrayList<>();

        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());

            times.add(new int[]{start, 1}); // 강의 시작: +1
            times.add(new int[]{end, -1}); // 강의 종료: -1
        }

        // 1️⃣ 정렬: 시간 기준 오름차순, 같은 시간이라면 종료(-1)가 시작(+1)보다 앞에 오도록
        Collections.sort(times, (a, b) -> {
            if (a[0] == b[0]) return Integer.compare(a[1], b[1]); // 같은 시간이면 종료(-1) 먼저
            return Integer.compare(a[0], b[0]); // 시간 기준 정렬
        });

        // 2️⃣ 스위핑 수행
        int maxRooms = 0;  // 최대 필요 강의실 개수
        int currentRooms = 0;  // 현재 진행 중인 강의 개수

        for (int[] event : times) {
            currentRooms += event[1]; // 시작이면 +1, 종료면 -1
            maxRooms = Math.max(maxRooms, currentRooms); // 최대값 갱신
        }

        System.out.println(maxRooms); // 최소 필요한 강의실 수 출력
    }
}
