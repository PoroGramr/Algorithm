import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        int[] count = new int[26];

        for (int i = 0; i < s.length(); i++){
            char c = s.charAt(i);
            count[c - 'a']++;
        }

        for(int i = 0; i < 26; i++){
            System.out.print(count[i]);
            System.out.print(" ");
        }
    }
}