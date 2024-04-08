public class prime_no {
    public static void main(String[] args) {
        int num=17;
        int flag = 0;

        for(int i=num-1; i>1; i--) {
            if(num%i==0) {
                System.out.println("Not Prime");
                flag++;
                break;
            }
        }
        if(flag==0)
            System.out.println("Prime");
    }
}
