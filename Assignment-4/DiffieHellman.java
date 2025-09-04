import java.math.BigInteger;
import java.util.*;

public class DiffieHellman {
    
    static Set<BigInteger> primeFactors(BigInteger n) {
        Set<BigInteger> factors = new HashSet<>();
        BigInteger two = BigInteger.valueOf(2);

        while (n.mod(two).equals(BigInteger.ZERO)) {
            factors.add(two);
            n = n.divide(two);
        }

        BigInteger i = BigInteger.valueOf(3);
        while (i.multiply(i).compareTo(n) <= 0) {
            while (n.mod(i).equals(BigInteger.ZERO)) {
                factors.add(i);
                n = n.divide(i);
            }
            i = i.add(two);
        }

        if (n.compareTo(BigInteger.ONE) > 0) {
            factors.add(n);
        }
        return factors;
    }

    static boolean isPrimitiveRoot(BigInteger g, BigInteger p) {
        BigInteger phi = p.subtract(BigInteger.ONE); // p-1
        Set<BigInteger> factors = primeFactors(phi);

        for (BigInteger factor : factors) {
            BigInteger exp = phi.divide(factor);
            if (g.modPow(exp, p).equals(BigInteger.ONE)) {
                return false; 
            }
        }
        return true;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter a prime number (p): ");
        BigInteger p = sc.nextBigInteger();

        System.out.print("Enter a primitive root candidate (g): ");
        BigInteger g = sc.nextBigInteger();

        if (!isPrimitiveRoot(g, p)) {
            System.out.println("The given g = " + g + " is NOT a primitive root modulo p = " + p);
            sc.close();
            return;
        } else {
            System.out.println("The given g = " + g + " is a VALID primitive root modulo p = " + p);
        }

        System.out.print("Enter private key for A: ");
        BigInteger a = sc.nextBigInteger();

        System.out.print("Enter private key for B: ");
        BigInteger b = sc.nextBigInteger();

        BigInteger A_pub = g.modPow(a, p);
        BigInteger B_pub = g.modPow(b, p);

        BigInteger sharedKeyA = B_pub.modPow(a, p);
        BigInteger sharedKeyB = A_pub.modPow(b, p);

        System.out.println("\nPublic values:");
        System.out.println("p (prime): " + p);
        System.out.println("g (base): " + g);

        System.out.println("\nA's public key: " + A_pub);
        System.out.println("B's public key: " + B_pub);

        System.out.println("\nShared secret calculated by A: " + sharedKeyA);
        System.out.println("Shared secret calculated by B: " + sharedKeyB);

        if (sharedKeyA.equals(sharedKeyB)) {
            System.out.println("\nKey exchange successful! Shared secret is: " + sharedKeyA);
        } else {
            System.out.println("\nKey exchange failed!");
        }

        sc.close();
    }
}