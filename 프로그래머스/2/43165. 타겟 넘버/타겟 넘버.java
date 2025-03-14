import java.io.*;
import java.util.*;

class Solution {
    int answer;
    public int solution(int[] numbers, int target) {
        
        dfs(numbers, target,0,0);
        return answer;
    }
    
    public void dfs(int[] numbers, int target, int curIdx, int curNum){
        if (curIdx >=numbers.length){
            if (curNum == target){
                answer += 1;
            }
            return;
        }
        dfs(numbers, target, curIdx+1, curNum + numbers[curIdx]);
                
        dfs(numbers, target, curIdx+1, curNum - numbers[curIdx]);
    }
}