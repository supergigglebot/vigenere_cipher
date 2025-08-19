def vigenere_cipher(text, keyword, mode="encode"):
    result = []
    keyword = keyword.upper()
    text = text.upper()
    keyword_length = len(keyword)
    
    for i, char in enumerate(text):
        if char.isalpha():
            shift = ord(keyword[i % keyword_length]) - ord('A')
            if mode == "decode":
                shift = -shift
            new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            result.append(new_char)
        else:
            result.append(char)
    return "".join(result)


def main():
    mode = input("Would you like to encode or decode? ").strip().lower()
    while mode not in ["encode", "decode"]:
        mode = input("Please enter 'encode' or 'decode': ").strip().lower()
    
    keyword = input("Enter keyword: ").strip()
    text = input("Enter text: ").strip()

    output = vigenere_cipher(text, keyword, mode)
    print(f"\n{mode.capitalize()}d text: {output}")


if __name__ == "__main__":
    main()
