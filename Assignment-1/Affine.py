def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x

def affine_encrypt(text, a, b):
    result = ""
    for c in text:
        if c.isalpha():
            base = 65 if c.isupper() else 97
            result += chr((a * (ord(c) - base) + b) % 26 + base)
        else:
            result += c
    return result

#formula used:(a*x +b)mod26  where a and b are prime no from 1 to 26


def affine_decrypt(text, a, b):
    a_inv = mod_inverse(a, 26)
    result = ""
    for c in text:
        if c.isalpha():
            base = 65 if c.isupper() else 97
            result += chr((a_inv * ((ord(c) - base) - b)) % 26 + base)
        else:
            result += c
    return result

if __name__ == "__main__":

    print("Affine encryption")
    a = int(input("Enter key 'a': "))
    b = int(input("Enter key 'b': "))
    text = input("Enter plaintext: ")

    encrypted = affine_encrypt(text, a, b)
    decrypted = affine_decrypt(encrypted, a, b)

    print("Encrypted:", encrypted)
    print("Decrypted:", decrypted)