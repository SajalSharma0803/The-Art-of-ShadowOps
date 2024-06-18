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
    mode = input("Enter 1 for encryption or enter 2 for decryption: ").strip().lower()
    if mode not in ["1", "2"]:
        print("Invalid choice. Please enter '1' or '2'.")
        return

    text = input("Enter the string: ").strip()

    key = int(input("Enter the key (an integer): ").strip())


    final = caesarcipher(text, key, mode)
    print(f"Resulting string: {final}")
    print(f"Length of resulting string: {len(final)}")

if __name__ == "__main__":
    main()
