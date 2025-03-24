import java.io.*;
import java.util.*;

public class Main {
	static long[] lines;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");

		// 가지고 있는 K개의 랜선, 필요한 랜선의 개수 N
		long K = Long.parseLong(st.nextToken());
		long N = Long.parseLong(st.nextToken());

		// 가지고 있는 랜선의 길이 배열
		lines = new long[(int) K];

		for(int i = 0; i < K; i++){
			st = new StringTokenizer(br.readLine(), " ");
			lines[i] = Long.parseLong(st.nextToken());
		}

		// 최대 랜선의 길이
		// 11개를 만들어야 해
		long left = 1;
		long right = Arrays.stream(lines).max().getAsLong();

		long result = 0;
		long mid = 0;

		while(left <= right){
			mid = (left + right) / 2L;
			long count = countCutLines(mid);
			if(count >= N ){
				result = mid;
				left = mid + 1;
			}
			else{
				right = mid - 1;
			}
		}

		System.out.println(result);
	}

	// mid 길이로 자를 때 몇 개 만들 수 있는지 계산하는 함수
	private static long countCutLines(long length) {
		long count = 0;
		for (long line : lines) {
			count += (line / length);
		}
		return count;
	}
}
