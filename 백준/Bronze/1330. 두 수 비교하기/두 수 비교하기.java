import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);

        int i = s.nextInt();
        int j = s.nextInt();
        if (i == j){
            System.out.println("==");
        }else if (i > j){
            System.out.println(">");
        }else{
            System.out.println("<");
        }


    }
}