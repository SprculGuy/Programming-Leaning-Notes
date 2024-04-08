public class factors_of_number {
    public static void main(String[] args) {
        int num = 6;
        System.out.printf("factors of %d are: ", num);
        for(int i=1; i<=num; i++) {
            if(num%i==0)
                System.out.printf("%d, ", i);
        }
    }
}
