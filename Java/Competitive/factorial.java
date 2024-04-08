public class factorial {
    public static void main(String[] args) {
        int num = 5;
        int factorial = 1;
        for(int i=num;i>1;i--)
            factorial *= i;
        System.out.printf("Factorial of %d = %d",num ,factorial);
    }
}
