import java.util.Scanner;
import java.lang.System;

public class App
{
    static int numOxygenCylinder(int[] oxyegen, int limit)
    {
        int sum = 0;
        for(int i : oxyegen)
        {
            sum+=i;
        }

        if(sum % limit == 0) 
            return sum/limit;
        else 
            return (sum/limit)+1;
    }

    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();               // 2
        int limit = sc.nextInt();           // 1 

        int[] oxygen = new int[n];
        for(int i=0; i<n; i++) 
        {
           oxygen[i] = sc.nextInt();           // oxygen[0] = 1  ,  oxygen[1] = 2 
        }
        System.out.println(numOxygenCylinder(oxygen, limit));  
    }
}