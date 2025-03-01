import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");

        long X = Long.parseLong(input[0]); // 총 게임 수
        long Y = Long.parseLong(input[1]); // 이긴 게임 수

        long Z = (Y * 100) / X; // 현재 승률

        // 승률이 변하지 않는다면 -1 출력
        if (Z >= 99) {
            System.out.println(-1);
            return;
        }

        long left = 0, right = X, answer = -1;

        while (left <= right) {
            long mid = (left + right) / 2;
            long newZ = ((Y + mid) * 100) / (X + mid);

            if (newZ > Z) { // 승률이 증가하면 mid를 줄여야 함
                answer = mid;
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }

        System.out.println(answer);
    }
}
