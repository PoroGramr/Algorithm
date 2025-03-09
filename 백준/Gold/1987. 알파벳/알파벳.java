import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;
 
 
public class Main {
	static int oy, ox;
	static char[][] board;
	static int[] visited = new int[26];
	static int[] dx = {-1, 1, 0, 0}; // 상하좌우 이동
    static int[] dy = {0, 0, -1, 1};
	static int answer = 0;

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");

		oy = Integer.parseInt(st.nextToken());
		ox = Integer.parseInt(st.nextToken());
		board = new char[oy][ox];
		

		for(int i = 0; i < oy; i++) {
			board[i] = br.readLine().toCharArray(); // 한 줄씩 입력받아 배열에 저장
		}
		

		dfs(0,0,1);


		System.out.println(answer);
	}


	public static void dfs(int x, int y, int depth){
		visited[board[y][x] - 'A'] = 1;
		answer= Math.max(answer,depth);

		// 4방향 이동
        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            // 범위 내에 있고, 방문하지 않은 알파벳이면 이동
            if (nx >= 0 && nx < ox && ny >= 0 && ny < oy && visited[board[ny][nx] - 'A']==0) {
                dfs(nx, ny, depth + 1);
            }

			
        }

		visited[board[y][x] - 'A'] = 0;
	}

	
}