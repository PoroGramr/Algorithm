import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        long N = sc.nextLong();
        int A = sc.nextInt();
        int B = sc.nextInt();
        int C = sc.nextInt();

        double low = 0;
        double high = Math.min(A, Math.min(B, C));
        double mid = 0;

        // 이분 탐색 (실수)
        for (int i = 0; i < 100; i++) {  // 충분히 반복해서 정밀도 확보
            mid = (low + high) / 2;
            if (countCubes(A, B, C, mid) >= N) {
                low = mid; // 가능한 경우 -> 더 큰 길이를 시도
            } else {
                high = mid; // 불가능한 경우 -> 더 작은 길이를 시도
            }
        }

        System.out.printf("%.10f\n", low); // 정확도 요구 높음
    }

    static long countCubes(int A, int B, int C, double len) {
        return (long)(A / len) * (long)(B / len) * (long)(C / len);
    }
}