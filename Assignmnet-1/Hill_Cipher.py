import numpy as np

def char_to_num(char):
    return ord(char.upper()) - ord('A')

def num_to_char(num):
    return chr(int(num % 26) + ord('A'))

def prepare_text(text):
    text = text.upper().replace(" ", "")
    if len(text) % 2 != 0:
        text += 'X'
    return text

def encrypt(message, key_matrix):
    message = prepare_text(message)
    cipher = ''
    for i in range(0, len(message), 2):
        pair = [char_to_num(message[i]), char_to_num(message[i+1])]
        result = np.dot(key_matrix, pair) % 26
        cipher += ''.join(num_to_char(n) for n in result)
    return cipher

def mod_inv_matrix(matrix, mod):
    det = int(np.round(np.linalg.det(matrix))) % mod
    try:
        det_inv = pow(det, -1, mod)
    except ValueError:
        raise ValueError("Key matrix is not invertible. Try another matrix.")
    adj = np.round(det * np.linalg.inv(matrix)).astype(int) % mod
    return (det_inv * adj) % mod

def decrypt(cipher, key_matrix):
    inv_key = mod_inv_matrix(key_matrix, 26)
    decrypted = ''
    for i in range(0, len(cipher), 2):
        pair = [char_to_num(cipher[i]), char_to_num(cipher[i+1])]
        result = np.dot(inv_key, pair) % 26
        decrypted += ''.join(num_to_char(n) for n in result)
    return decrypted

plaintext = input("Enter the plaintext: ")

key_chars = input("Enter the 4-letter key (e.g., 'GYBN'): ").upper()

if len(key_chars) != 4 or not key_chars.isalpha():
    raise ValueError("Key must be exactly 4 alphabetic characters.")

key_nums = [char_to_num(c) for c in key_chars]
key_matrix = np.array(key_nums).reshape(2, 2)

try:
    ciphertext = encrypt(plaintext, key_matrix)
    decrypted_text = decrypt(ciphertext, key_matrix)

    print("\n--- Results ---")
    print("Plaintext :", plaintext.upper())
    print("Key Matrix:\n", key_matrix)
    print("Encrypted :", ciphertext)
    print("Decrypted :", decrypted_text)

except ValueError as e:
    print(f"\nError: {e}")