import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int X = sc.nextInt();

        int arr[] = new int[N];

        for(int a = 0; a < N; a++){
            arr[a] = sc.nextInt();
        }        

        for(int b = 0; b < N; b++){
            if (arr[b] < X){
                System.out.print(arr[b]);
                System.out.print(" ");
            }
        }


    }
}