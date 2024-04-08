// 454 is palindoreme number
public class palindrome {
    public static void main(String[] args){
        int number, digit, reverse=0, original;
        number = 455;
        original = number;

        while(number > 0) {
            digit = number % 10;
            reverse = reverse * 10 + digit;
            number /= 10;
        }

        if(original==reverse)
            System.out.println("Palindrome");
        else
            System.out.println("Not Palindrome");
    }
    
}
