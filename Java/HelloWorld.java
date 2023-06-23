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

        System.out.print("Enter Your full name : ");
        String Name = sc.nextLine();
        System.out.print("Enter Your Age : ");
        int age = sc.nextInt();
        System.out.print("Enter Your Hight(in cm) : ");
        float height = sc.nextFloat();

        System.out.println("Hello " + Name + ", age " + age +", have a good day...");

        System.out.print("Enter Your first name : ");
        String fullname = sc.next();

        System.out.println("Hello " + fullname + ", have a good day...");
        System.out.printf("Name: %s, Age: %d, Height: %.2f\n", name, age, height);
        System.out.println(String.format("Name: %s, Age: %d, Height: %.2f", name, age, height));

        sc.close();
    }                                               
}                                                   
