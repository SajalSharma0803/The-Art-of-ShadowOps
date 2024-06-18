def caesarcipher(text, key, mode):
    result = ""
    if mode == "2":
        key = -key

    for char in text:
        if char.isalpha():
            if char.isupper():
                shift = 65
            else:
                shift = 97
            result += chr((ord(char) - shift + key) % 26 + shift)
        else:
            result += char

    return result

def main():
    import os

    inputfile = input("Enter the input file name (including extension): ").strip()
    if not os.path.isfile(inputfile):
        print(f"File '{inputfile}' does not exist.")
        return

    mode = input("Enter 1 for encryption or enter 2 for decryption: ").strip()
    if mode not in ["1", "2"]:
        print("Invalid choice. Please enter '1' or '2'.")
        return
    key = int(input("Enter the key (an integer): ").strip())
    
    with open(inputfile, 'r', encoding='utf-8') as file:
        text = file.read()

    final = caesarcipher(text, key, mode)
    
    outputfile = "output.txt"
    with open(outputfile, 'w', encoding='utf-8') as file:
        file.write(final)

    print(f"Resulting text has been written to '{outputfile}'.")
    print(f"Length of resulting text: {len(final)}")

if __name__ == "__main__":
    main()
