public class fibonacci_series {
    public static void main(String[] args) {
        int n = 5;
        int a=1,b=1;

        if(n==0)
            System.out.println(a);
        else if(n==1)
            System.out.println(a+" "+b);
        else{            
            System.out.print(a+" "+b);
            for(int i=2; i<=n; i++){
                int c = a+b;
                System.out.print(" "+c);
                a=b;
                b=c;
            }
        }

    }
}
