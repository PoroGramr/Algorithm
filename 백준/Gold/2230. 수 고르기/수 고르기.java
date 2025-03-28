import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static int n, m;
    static int[] nums;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        nums = new int[n];
        for (int i = 0; i < n; i++) {
            nums[i] = Integer.parseInt(br.readLine());
        }

        Arrays.sort(nums); // 정렬 필수

        int i = 0, j = 0;
        int minValue = Integer.MAX_VALUE;

        while (j < n) {
            if (i == j) {
                j++; // 같은 수일 경우 의미 없으니 j 증가
                continue;
            }

            int diff = nums[j] - nums[i];

            if (diff < m) {
                j++;
            } else {
                minValue = Math.min(minValue, diff);
                i++;
            }
        }

        System.out.println(minValue);
    }
}
