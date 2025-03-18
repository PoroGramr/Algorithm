import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        
        int testCaseCount = Integer.parseInt(br.readLine()); // 테스트 케이스 개수

        for (int t = 0; t < testCaseCount; t++) {
            // 배열 크기 입력
            StringTokenizer st = new StringTokenizer(br.readLine());
            int sizeA = Integer.parseInt(st.nextToken());
            int sizeB = Integer.parseInt(st.nextToken());

            // 배열 입력
            int[] A = new int[sizeA];
            int[] B = new int[sizeB];

            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < sizeA; i++) {
                A[i] = Integer.parseInt(st.nextToken());
            }

            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < sizeB; i++) {
                B[i] = Integer.parseInt(st.nextToken());
            }

            // 정렬
            Arrays.sort(A);
            Arrays.sort(B);

            int count = 0;
            int bIndex = 0; // B 배열에서 탐색할 인덱스

            // A의 원소를 하나씩 확인하며 B에서 작은 개수 세기
            for (int aIndex = 0; aIndex < sizeA; aIndex++) {
                while (bIndex < sizeB && B[bIndex] < A[aIndex]) {
                    bIndex++; // B의 포인터를 이동
                }
                count += bIndex; // 현재까지 B에서 작은 원소 개수를 더함
            }

            sb.append(count).append("\n");
        }
        System.out.print(sb);
    }
}
