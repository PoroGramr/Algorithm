import java.util.*;

class Solution {
    public int[] solution(long n) {
        String str = Long.toString(n);  // 숫자를 문자열로 변환
        int len = str.length();
        int[] answer = new int[len];    // 결과 배열 생성
        
        for (int i = 0; i < len; i++) {
            answer[i] = str.charAt(len - 1 - i) - '0';  // 문자 → 숫자로 변환
        }
        
        return answer;
    }
}
