import java.io.*;
import java.util.*;

public class Main {
	static int num;
	static int countCom;
	static int[][] graph;
	static boolean[] visited;
	static int count;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");

		// 컴퓨터의 수
		num = Integer.parseInt(st.nextToken());

		// 컴퓨터 쌍의 수
		st = new StringTokenizer(br.readLine(), " ");
		countCom = Integer.parseInt(st.nextToken());

		graph = new int[num + 1][num + 1];
		visited = new boolean[num + 1];

		for (int i = 0; i < countCom; i++) {
			st = new StringTokenizer(br.readLine(), " ");
			int src = Integer.parseInt(st.nextToken());
			int dst = Integer.parseInt(st.nextToken());
			graph[src][dst] = 1;
			graph[dst][src] = 1;
		}
		dfs(1);
		System.out.println(count - 1);
	}

	static void dfs(int node){
		visited[node] = true;
		count++;
		for (int i = 1; i <= num; i++){
			if(graph[node][i] == 1 && !visited[i]){
				dfs(i);
			}
		}
	}



}
