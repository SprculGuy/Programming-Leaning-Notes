public class largest_from_3_variables {
    public static void main(String[] args) {
        int a = 12, b = 15, c = 20;
        if(a>=b && a>=c) 
            System.out.printf("Largest number is %d", a);
        else if(b>=c) 
            System.out.printf("Largest number is %d", b);
        else 
            System.out.printf("Largest number is %d", c);
    }
}
