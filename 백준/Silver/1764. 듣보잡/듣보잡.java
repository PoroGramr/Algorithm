
import java.io.*;
import java.util.*;
 
 
public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");

		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());


		HashSet<String> unheard = new HashSet<>();
		ArrayList<String> result = new ArrayList<>();

		for (int i = 0; i < N; i++){
			unheard.add(br.readLine());
		}

		for (int i = 0; i < M; i++){
			String unsee = br.readLine();
			if(unheard.contains(unsee)){
				result.add(unsee);
			}
		}

		Collections.sort(result);

		StringBuilder sb = new StringBuilder();
		sb.append(result.size()).append("\n");
		for(int i = 0; i < result.size();i++){
			sb.append(result.get(i)).append("\n");
		}
		System.out.println(sb);




	}


	
}