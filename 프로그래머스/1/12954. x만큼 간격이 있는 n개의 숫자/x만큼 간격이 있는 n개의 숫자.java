class Solution {
    public long[] solution(int x, int n) {
        long[] answer = new long[n];
        long up = x ;
        
        for(int i = 0; i < n; i++){
            answer[i] = up;
            up += x;
        }
        
        return answer;
    }
}