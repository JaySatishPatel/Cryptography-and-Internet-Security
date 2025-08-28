from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import binascii

def pad(data):
    pad_len = 16 - (len(data) % 16)
    return data + bytes([pad_len]) * pad_len

def unpad(data):
    pad_len = data[-1]
    return data[:-pad_len]

if __name__ == "__main__":
    plaintext = input("Enter plaintext: ").encode()

    key = get_random_bytes(16)
    print("AES Key (hex):", binascii.hexlify(key).decode())

    iv = get_random_bytes(16)
    print("IV (hex):", binascii.hexlify(iv).decode())

    cipher = AES.new(key, AES.MODE_CBC, iv)

    padded_text = pad(plaintext)
    ciphertext = cipher.encrypt(padded_text)
    print("Ciphertext (hex):", binascii.hexlify(ciphertext).decode())

    decipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_text = unpad(decipher.decrypt(ciphertext))
    print("Decrypted text:", decrypted_text.decode())