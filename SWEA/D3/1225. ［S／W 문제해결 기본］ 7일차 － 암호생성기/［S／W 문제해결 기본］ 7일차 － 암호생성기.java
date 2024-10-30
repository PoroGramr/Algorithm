import java.util.ArrayList;
import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        for(int i = 1; i <=10; i++){
            int n = scanner.nextInt();
            scanner.nextLine();

            ArrayList<Integer> data = new ArrayList<Integer>();
            String[] input = scanner.nextLine().split(" ");

            for(String s : input){
                data.add(Integer.parseInt(s));
            }

            int s = 0;
            for (;;) {
                int tmp = data.remove(0);
                tmp -= (s + 1);
                s = (s + 1) % 5;

                if (tmp <= 0) {
                    data.add(0);
                    break;
                }
                else{
                    data.add(tmp);
                }
            }
            System.out.print("#" + i +  " ");
            for(int k =0; k < data.size(); k++){
                System.out.print(data.get(k) + " ");
            }
            System.out.println();

        }
    }
}
