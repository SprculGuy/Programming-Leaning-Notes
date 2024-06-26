import java.lang.Math;

class prime_factors {
	// A function to print all prime factors
	// of a given number n
	public static void primeFactors(int n)
	{
		// Print the number of 2s that divide n
		while (n % 2 == 0) {                    // for even numbers
			System.out.print(2 + " ");
			n /= 2;
		}

		// n must be odd at this point. So we can skip one element (i+=2)
		for (int i=3; i<=Math.sqrt(n); i+=2) {
			// While i divides n, print i and divide n
			while (n % i == 0) {
				System.out.print(i + " ");
				n /= i;
			}
		}

		
		if (n > 2) // This condition is to handle the case when n is a prime number greater than 2
			System.out.print(n);
	}

	public static void main(String[] args)
	{
		int n = 3178;
		primeFactors(n);
	}
}
