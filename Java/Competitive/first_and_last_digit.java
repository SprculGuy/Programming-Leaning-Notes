// package Competitive;

public class first_and_last_digit {
    public static void main(String[] args) {
        int num = 7123456;
        int first_digit = num;
        int last_digit = num % 10;
        while(first_digit>=10)
            first_digit /= 10;
        System.out.printf("First Digit - %d \nLast Digit - %d",first_digit, last_digit);
    }    
}
