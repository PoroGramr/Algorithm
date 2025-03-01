/** 
 * @요구사항
 * 상근이는 나무 M미터가 필요하다. 새로산 목재 절단기를 이용해서 나무를 구할것이다.
 * 절단기는 다음과 같이 동작.
 * 절단기에 높이 H를 지정. 높이를 지정하면 톱날이 땅으로부터 H미터 위로 올라감.
 * 따라서, 높이가 H보다 큰 나무믄 H 윗 부분이 잘릴 것이고.
 *       높이가 H보다 작은 아무는 잘리지 않는다.
 * 
 * 상근이는 나무를 필요한 만큼만 집으로 가져가려고 한다. 이떄, 적어도 M미터를 가져가기 위해
 * 설정할 수 있는 높이의 최댓값은?
 * 
 * @ 입력
 * N : 나무의 수 M : 가져가려고 하는 나무의 길이
 * [] : 나무의 높이 배열
 * 
 * @아이디어
 * 
 * 입력 값이 1억을 넘어간다 -> 완전 탐색 불가 -> 이진 탐색으로 풀어야 함
 * 
 * 탐색 left = 0 right = 나무의 높이 중 최대 길이
 * while(left <= right)
 * {
 *  mid = (left +right) / 2;
 *  hometree = cutTree(mid)
 * }
 * if (newM > M){
 *  answer = newM
 * left = mid + 1
 * } else{
 * right = mid - 1}
 * 
 * sout(answer)
*/

import java.io.*;
import java.util.*;


public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");
        
        // 나무의 수, 집으로 가져가려는 나무의 길이
        long treeCount = Long.parseLong(input[0]);
        long backTree = Long.parseLong(input[1]);
        long answer = 0;

        // 나무 높이 배열
        String[] treeInput = br.readLine().split(" ");
        long[] trees = new long[(int)treeCount];

        for(int i = 0; i < treeCount; i++){
            trees[i] = Long.parseLong(treeInput[i]);
        }

        long left = 0;
        long right = Arrays.stream(trees).max().getAsLong();

        while(left <= right){
            long mid = (left + right) / 2;
            long curBackTree = getWood(trees, mid);

            if (curBackTree >= backTree){
                answer = mid;
                left = mid + 1;
            }else{
                right = mid - 1;
            }
            
        }


        System.out.println(answer);

        br.close();
    }

    /**
     * 집에 들고갈 수 있는 나무의 길이 리턴
     */
    public static long getWood(long[] trees, long cutHeight){
        long getTree = 0;

        for (int i = 0; i < trees.length; i++){
            if (trees[i] >= cutHeight){
                getTree += trees[i] - cutHeight;
            }
        }
        return getTree;
    }
}
