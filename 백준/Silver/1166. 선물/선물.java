import java.io.*;
import java.util.*;

public class Main {
	static long[] lines;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");

		long N = Long.parseLong(st.nextToken());
		int A = Integer.parseInt(st.nextToken());

		int B = Integer.parseInt(st.nextToken());

		int C = Integer.parseInt(st.nextToken());

		double left = 0;
		double right = Math.min(A, Math.min(B, C));
		double mid = 0;

		for (int i = 0; i < 100; i ++) {
			mid = (left + right) / 2;
			if (countCubes(A, B, C, mid) >= N) {
				left = mid;
			} else {
				right = mid;
			}

		}
		System.out.printf("%.10f\n", left); // 정확도 요구 높음}//}
	}

	static long countCubes(int A, int B, int C, double len) {
		return (long)(A / len) * (long)(B / len) * (long)(C / len);
	}
}
