public class leap_year {
    public static void main(String[] args) {
        int year = 2005;
        if(year%4==0 && year%100!=0)
            System.out.printf("%d is a Leap year.", year);
        else if(year%400==0)    
            System.out.printf("%d is a Leap year.", year);
        else
            System.out.printf("%d is a not Leap year.", year);
    }
}
