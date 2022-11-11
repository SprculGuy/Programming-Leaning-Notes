import java.util.Scanner;

/*
    This is my 
    first Java 
    program
*/


public class HelloWorld                    // ClassName - PascalConvention
{                                                   // void   - return type of function
    public static void main(String[] args)          // public - scope of function           // functionName - camelCaseConvention
    {                                               // static - gives ability to get exicuted without creating any object of class
        String name = "Ankit";                      // args   - argument defining
        System.out.println("Hello World");                      // to treat the function as it is outside of class 
        System.out.println(name);                               // println gives new line after execution of print
        System.out.print("Hello");                       
        System.out.println(name);

        Scanner sc = new Scanner(System.in);
        System.out.print("Enter Your first name : ");
        String Name = sc.next();
        System.out.print("Enter Your Age : ");
        int age = sc.nextInt();
        System.out.println("Hello " + Name + ", age " + age +", have a good day...");

        int age1 = 0;

        while(true){
            if(sc.hasNextInt()){
                age1 = sc.nextInt();
                break;
            }
        }
        System.out.print(age1);
        
        System.out.print("Enter Your full name : ");
        String fullName = sc.nextLine();
        System.out.println("Hello " + fullName + ", have a good day...");
        // System.out.printf( %s"Hello <fullName>, have a good day...", fullName);
        sc.close();
    }                                               
}                                                   
