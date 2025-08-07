def encryption(pt, key):
    cipher = ""
    for ch in pt:
        if ch.isalpha():
            shift = key % 26
            if ch.islower():
                cipher += chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
            else:
                cipher += chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
        else:
            cipher += ch
    return cipher

def decryption(ct, key):
    plain = ""
    for ch in ct:
        if ch.isalpha():
            shift = key % 26
            if ch.islower():
                plain += chr((ord(ch) - ord('a') - shift) % 26 + ord('a'))
            else:
                plain += chr((ord(ch) - ord('A') - shift) % 26 + ord('A'))
        else:
            plain += ch
    return plain

if __name__ == "__main__": 
    print("Caesar Cipher")
    pt = input("Enter the plaintext: ")
    key = int(input("Enter the key: "))


    print("plaintext entered:", pt)
    cipher_text = encryption(pt, key)

    print("Ciphertext:", cipher_text)

    decrypted_text = decryption(cipher_text, key)
    
    print("Decrypted text:", decrypted_text)