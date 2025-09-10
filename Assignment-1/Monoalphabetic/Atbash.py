def atbashencryption(text):
    result = ""
    for char in text:
        if char.isupper():
            result += chr(65 + (25 - (ord(char) - 65)))
        elif char.islower():
            result += chr(97 + (25 - (ord(char) - 97)))
        else:
            result += char
    return result
print("Atbash cipher")
pt = input("Enter the text: ")
cipher = atbashencryption(pt)
print("Atbash cipher:", cipher)