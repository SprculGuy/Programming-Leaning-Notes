public class LCM_and_GCD {
    public static void main(String[] args) {
        int a=10, b=15;
        int min, max, LCM=a*b, GCD=-1;
        
        if(a<b){
            min=a;
            max=b;
        }
        else{
            min=b;
            max=a;    
        }
        
        
        for(int i=min;i>0;i--){
            if(a%i==0 && b%i==0){
                GCD=i;
                break;
            }
        }

        for(int i=max;i<a*b;i++){
            if(i%a==0 && i%b==0){
                LCM=i;
                break;
            }
        }
        
        System.out.printf("%d, %d \nLCM=%d \nGCD=%d", a, b, LCM, GCD);
    }
}
