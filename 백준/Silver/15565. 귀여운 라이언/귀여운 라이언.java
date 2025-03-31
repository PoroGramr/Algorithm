import java.io.*;
import java.util.*;

public class Main {
	static int N, K;
	static int[] dolls;
	static int result;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		// N개의 인형이 일렬로 놓여 있음
		N = Integer.parseInt(st.nextToken());

		// K개 이상의 라이언 인형의 연속된 집합 크기
		K = Integer.parseInt(st.nextToken());

		dolls = new int[N];

		result = Integer.MAX_VALUE;

		st = new StringTokenizer(br.readLine(), " ");
		for(int i =0; i < N; i++){
			dolls[i] = Integer.parseInt(st.nextToken());
		}

		int left = 0, right = 0, ryanCount = 0;
		int minLength = Integer.MAX_VALUE;

		while (right < N) {
			if (dolls[right] == 1) ryanCount++;

			// 라이언 인형이 K개 이상이면 윈도우 축소 가능
			while (ryanCount >= K) {
				minLength = Math.min(minLength, right - left + 1);
				if (dolls[left] == 1) ryanCount--;
				left++;
			}
			right++;
		}

		System.out.println(minLength == Integer.MAX_VALUE ? -1 : minLength);


	}
}
