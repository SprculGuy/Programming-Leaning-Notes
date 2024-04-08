public class sum_of_n {
    public static void main(String[] args){
        int n = 5;
        
        if(n<1){
            System.out.println("Invalid Input");
            return;
        }

        int sum = (n*(n+1))/2;
        System.out.printf("Sum of %d natural numbers = %d", n, sum);

    }
    
}
