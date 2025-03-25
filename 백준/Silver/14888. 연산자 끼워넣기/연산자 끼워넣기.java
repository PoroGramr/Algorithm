import java.io.*;
import java.util.*;

public class Main {
    static int N;
    static int[] numbers;
    static int[] operators; // +, -, *, /
    static int maxResult = Integer.MIN_VALUE;
    static int minResult = Integer.MAX_VALUE;
    static List<Integer> opList = new ArrayList<>(); // 연산자 리스트

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        numbers = new int[N];

        // 숫자 입력
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            numbers[i] = Integer.parseInt(st.nextToken());
        }

        // 연산자 개수 입력 (+, -, *, / 순서)
        st = new StringTokenizer(br.readLine());
        operators = new int[4];
        for (int i = 0; i < 4; i++) {
            operators[i] = Integer.parseInt(st.nextToken());
        }

        // **연산자 리스트 생성**
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < operators[i]; j++) {
                opList.add(i); // {0:+, 1:-, 2:*, 3:/}
            }
        }

        // **연산자 순열 탐색 (nextPermutation 활용)**
        Collections.sort(opList); // 처음부터 사전순 정렬
        do {
            calculate(); // 현재 연산자 순열로 연산 수행
        } while (nextPermutation());

        // 결과 출력
        System.out.println(maxResult);
        System.out.println(minResult);
    }

    // **순열을 따라가면서 연산 수행**
    public static void calculate() {
        int result = numbers[0];

        for (int i = 0; i < opList.size(); i++) {
            int operator = opList.get(i);
            int num = numbers[i + 1];

            switch (operator) {
                case 0: result += num; break;
                case 1: result -= num; break;
                case 2: result *= num; break;
                case 3: result /= num; break; // 정수 나눗셈
            }
        }

        maxResult = Math.max(maxResult, result);
        minResult = Math.min(minResult, result);
    }

    // **nextPermutation (사전순 순열)**
    public static boolean nextPermutation() {
        int i = opList.size() - 1;
        while (i > 0 && opList.get(i - 1) >= opList.get(i)) {
            i--;
        }
        if (i == 0) return false;

        int j = opList.size() - 1;
        while (opList.get(i - 1) >= opList.get(j)) {
            j--;
        }

        // Swap
        Collections.swap(opList, i - 1, j);

        // 뒤쪽 정렬 (오름차순)
        Collections.reverse(opList.subList(i, opList.size()));

        return true;
    }
}
