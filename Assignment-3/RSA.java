import java.math.BigInteger;
import java.util.Scanner;

public class RSA {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter plaintext (as integer): ");
        BigInteger plaintext = sc.nextBigInteger();

        System.out.print("Enter prime number p: ");
        BigInteger p = sc.nextBigInteger();

        System.out.print("Enter prime number q: ");
        BigInteger q = sc.nextBigInteger();

        BigInteger n = p.multiply(q);

        BigInteger phi = (p.subtract(BigInteger.ONE)).multiply(q.subtract(BigInteger.ONE));

        BigInteger e = new BigInteger("65537");
        if (!phi.gcd(e).equals(BigInteger.ONE)) {
            e = new BigInteger("3"); 
        }

        BigInteger d = e.modInverse(phi);

        BigInteger ciphertext = plaintext.modPow(e, n);

        BigInteger decrypted = ciphertext.modPow(d, n);

        System.out.println("\nPublic key (e, n): (" + e + ", " + n + ")");
        System.out.println("Private key (d, n): (" + d + ", " + n + ")");
        System.out.println("Plaintext : " + plaintext);
        System.out.println("Ciphertext: " + ciphertext);
        System.out.println("Decrypted : " + decrypted);

        sc.close();
    }
}