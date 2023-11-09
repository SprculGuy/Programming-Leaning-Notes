import java.util.Scanner;

public class App {
    public static void main(String args[]) {
        System.out.print("Give a number: ");
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();
        int sum = num*(num+1)/2;
        System.out.println(sum);
        sc.close();

    }
}
