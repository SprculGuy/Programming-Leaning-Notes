public class no_of_digits {
    public static void main(String[] args) {
        int num = 1111;
        int count;
        for(count=1 ;num>10; count++){
            num/=10;
        }

//      int count = 1;
//      while(num>0){
//          num/=10;
//          count++;
//      }

        System.out.printf("No of digits : %d", count);
    }
}
