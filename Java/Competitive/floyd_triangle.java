public class floyd_triangle {
    public static void main(String[] args) {
        int number = 1;
        for(int i = 1; i<=3; i++) {
            for(int j = 1; j <= i; j++) {
                System.out.print(number++);
            }
            System.out.println();
        }
    }
}
