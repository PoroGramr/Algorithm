import java.io.*;
import java.util.*;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(bf.readLine(), " ");

		StringBuilder sb = new StringBuilder(); // 결과 저장 (입출력 최적화)

		// 테스트 케이스의 개수
		int T = Integer.parseInt(st.nextToken());

		// 테스트 케이스의 개수만큼 반복
		for (int i = 0; i < T; i++) {
			st = new StringTokenizer(bf.readLine(), " "); //
			// 지원자의 숫자
			int N = Integer.parseInt(st.nextToken());
			int[][] applier = new int[N][2];

			// 지원자의 데이터를 입력받음 (서류심사 성적, 어학점수 성적)
			for (int j = 0; j < N; j++) {
				st = new StringTokenizer(bf.readLine(), " "); //
				applier[j][0] = Integer.parseInt(st.nextToken());
				applier[j][1] = Integer.parseInt(st.nextToken());
			}

			// 1️⃣ 서류 성적 기준으로 정렬 (오름차순)
			Arrays.sort(applier, Comparator.comparingInt(a -> a[0]));

			// 2️⃣ 면접 등수를 비교하면서 선발
			int selectedCount = 1; // 첫 번째 지원자는 무조건 선발
			int minInterviewRank = applier[0][1]; // 첫 번째 지원자의 면접 등수

			for (int j = 1; j < N; j++) {
				if (applier[j][1] < minInterviewRank) { // 면접 성적이 더 좋은 경우
					selectedCount++;
					minInterviewRank = applier[j][1]; // 최소 면접 등수 업데이트
				}
			}

			sb.append(selectedCount).append("\n"); // 결과 저장
		}

		System.out.print(sb); // 최종 결과 출력
	}

}