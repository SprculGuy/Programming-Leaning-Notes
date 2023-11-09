// package Competitive;

import java.util.Scanner;

public class last_digit {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter a number: ");
        int num = sc.nextInt();
        int last_digit = num % 10;
        System.out.println(last_digit);

        sc.close();
    }    
}
