import java.io.*;

public class Main {
    static int[][] paper;
    static int white = 0, blue = 0; // 흰색(0)과 파란색(1) 개수

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine()); // 종이 크기 (2^k)
        
        paper = new int[N][N]; // 색종이 배열 선언

        // 색종이 정보 입력
        for (int i = 0; i < N; i++) {
            String[] line = br.readLine().split(" ");
            for (int j = 0; j < N; j++) {
                paper[i][j] = Integer.parseInt(line[j]);
            }
        }

        // 분할 정복 시작
        divide(0, 0, N);
        
        // 결과 출력
        System.out.println(white);
        System.out.println(blue);
    }

    // 분할 정복 메서드 (색종이를 나누는 함수)
    public static void divide(int row, int col, int size) {
        if (isSameColor(row, col, size)) { // 현재 영역이 같은 색인지 체크
            if (paper[row][col] == 0) white++; // 흰색
            else blue++; // 파란색
            return;
        }

        // 4개의 영역으로 나눠서 재귀 호출
        int newSize = size / 2;
        divide(row, col, newSize);             // 왼쪽 위
        divide(row, col + newSize, newSize);   // 오른쪽 위
        divide(row + newSize, col, newSize);   // 왼쪽 아래
        divide(row + newSize, col + newSize, newSize); // 오른쪽 아래
    }

    // 해당 영역이 모두 같은 색인지 확인하는 함수
    public static boolean isSameColor(int row, int col, int size) {
        int color = paper[row][col]; // 첫 번째 색 저장
        for (int i = row; i < row + size; i++) {
            for (int j = col; j < col + size; j++) {
                if (paper[i][j] != color) return false; // 다른 색이 있으면 false
            }
        }
        return true; // 모두 같은 색이면 true
    }
}
