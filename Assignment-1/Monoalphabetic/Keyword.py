def generate_key_alphabet(keyword):
    keyword = "".join(sorted(set(keyword), key=keyword.index))  
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    remaining = "".join([c for c in alphabet if c not in keyword.upper()])
    return keyword.upper() + remaining

def encrypt(text, keyword):
    key_alphabet = generate_key_alphabet(keyword)
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    for char in text:
        if char.isalpha():
            base = char.isupper()
            idx = alphabet.index(char.upper())
            enc = key_alphabet[idx]  
            result += enc if base else enc.lower()
        else:
            result += char
    return result

if __name__ == "__main__":
    print("keyword cipher encryption")
    text = input("Enter the text: ")
    keyword = input("Enter the keyword: ")
    encrypted = encrypt(text, keyword)
    print("Encrypted:", encrypted)