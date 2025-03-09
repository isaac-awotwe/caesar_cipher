# Import and print logo
from art import logo

print(logo)


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar_cipher(original_text, shift_amount, encode_or_decode):
    if encode_or_decode == "decode":
        shift_amount*=-1
    cipher_text = ""
    for letter in original_text:
        if letter not in alphabet:
            cipher_text+=letter
        else:
            shifted_position = (alphabet.index(letter) + shift_amount) % len(alphabet)
            cipher_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {cipher_text}")


run_again = True


while run_again:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar_cipher(original_text = text, shift_amount = shift, encode_or_decode = direction)

    run_again_question = input("Type 'yes' if you want to go again. Otherwise type 'no.'\n").lower()

    if run_again_question == "no":
        print("Goodbye")
        run_again = False

