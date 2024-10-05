public class day_before_n_days {
    public static void main(String[] args) {
        int day = 3;
        int n = 11;
        if(n>7)
            n %= 7;
        day -= n;
        if(day<0)
            day += 7;

        switch (day) {
            case 0:
                System.out.println("Monday");
                break;
            case 1:
                System.out.println("Tuesday");
                break;
            case 2:
                System.out.println("Wednesday");
                break;
            case 3:
                System.out.println("Thursday");
                break;
            case 4:
                System.out.println("Friday");
                break;
            case 5:
                System.out.println("Saturday");
                break;
            case 6:
                System.out.println("Sunday");
                break;        
            default:
                System.out.println("Invalid");
        }
    }
    
}
