def vigenere_encrypt(plaintext, key):
    result = []
    key = key.upper()
    key_len = len(key)
    i = 0

    for c in plaintext:
        if c.isalpha():
            offset = 65 if c.isupper() else 97
            k = ord(key[i % key_len]) - 65
            result.append(chr((ord(c) - offset + k) % 26 + offset))
            i += 1
        else:
            result.append(c)
    return ''.join(result)
print("Vigenere Cipher")
text = input("Enter the text: ")
key = input("Enter the key: ")

print("Encrypted text:", vigenere_encrypt(text, key))