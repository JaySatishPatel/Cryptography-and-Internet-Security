from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
import binascii

def pad(data):
    pad_len = 8 - (len(data) % 8)
    return data + bytes([pad_len]) * pad_len

def unpad(data):
    pad_len = data[-1]
    return data[:-pad_len]

if __name__ == "__main__":
    plaintext = input("Enter plaintext: ").encode()

    key = get_random_bytes(8)
    print("DES Key (hex):", binascii.hexlify(key).decode())

    cipher = DES.new(key, DES.MODE_ECB)

    padded_text = pad(plaintext)
    ciphertext = cipher.encrypt(padded_text)
    print("Ciphertext (hex):", binascii.hexlify(ciphertext).decode())

    decipher = DES.new(key, DES.MODE_ECB)
    decrypted_text = unpad(decipher.decrypt(ciphertext))
    print("Decrypted text:", decrypted_text.decode())