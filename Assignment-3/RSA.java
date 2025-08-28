import java.math.BigInteger;
import java.nio.charset.StandardCharsets;
import java.util.Scanner;

public class RSA {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter plaintext (string): ");
        String message = sc.nextLine();

        BigInteger plaintext = new BigInteger(message.getBytes(StandardCharsets.UTF_8));

        System.out.print("Enter prime number p: ");
        BigInteger p = sc.nextBigInteger();

        System.out.print("Enter prime number q: ");
        BigInteger q = sc.nextBigInteger();

        BigInteger n = p.multiply(q);

        BigInteger phi = (p.subtract(BigInteger.ONE)).multiply(q.subtract(BigInteger.ONE));

        BigInteger e = new BigInteger("65537");
        if (!phi.gcd(e).equals(BigInteger.ONE)) {
            e = new BigInteger("3");  // fallback
        }

        BigInteger d = e.modInverse(phi);

        BigInteger ciphertext = plaintext.modPow(e, n);

        BigInteger decrypted = ciphertext.modPow(d, n);

        String decryptedMessage = new String(decrypted.toByteArray(), StandardCharsets.UTF_8);

        System.out.println("\nPublic key (e, n): (" + e + ", " + n + ")");
        System.out.println("Private key (d, n): (" + d + ", " + n + ")");
        System.out.println("Plaintext : " + message);
        System.out.println("Ciphertext: " + ciphertext);
        System.out.println("Decrypted : " + decryptedMessage);

        sc.close();
    }
}