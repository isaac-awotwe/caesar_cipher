# Import and print logo
from art import logo

print(logo)


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.

# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
#  by the shift amount and print the encrypted text.

# TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?

# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.


# TODO-1: Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as inputs.
# TODO-2: Inside the 'decrypt()' function, shift each letter of the 'original_text' *backwards* in the alphabet
#  by the shift amount and print the decrypted text.
# TODO-3: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
#  Use the value of the user chosen 'direction' variable to determine which functionality to use.

# def encrypt(original_text, shift_amount):
#     cipher_text = ""
#     for letter in original_text:
#         shifted_position = (alphabet.index(letter) + shift_amount) % len(alphabet)
#         cipher_text += alphabet[shifted_position]
#     print(f"Here is the encoded result: {cipher_text}")


#encrypt(original_text=text, shift_amount=shift)


# def decrypt(original_text, shift_amount):
#     cipher_text = ""
#     for letter in original_text:
#         original_position = (alphabet.index(letter) - shift_amount) % len(alphabet)
#         cipher_text += alphabet[original_position]
#     print(f"Here is the original text: {cipher_text}")


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

