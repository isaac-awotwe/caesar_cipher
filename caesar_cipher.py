alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.

# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
#  by the shift amount and print the encrypted text.

# TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?

# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.
alpha_length = len(alphabet)

def encrypt(original_text, shift_amount):
    encrypted_text = ""
    for letter in original_text:
        if letter not in alphabet:
            encrypted_text+=letter
        else:
            new_position = alphabet.index(letter) + shift_amount
            if new_position > alpha_length:
                encrypted_text += alphabet[(new_position % alpha_length) - 1]
            else:
                encrypted_text += alphabet[new_position]
    print(f"Here is the encoded result: {encrypted_text}")


def decrypt(original_text, shift_amount):
    decrypted_text = ""
    for letter in original_text:
        if letter not in alphabet:
            decrypted_text+=letter
        else:
            decrypted_text += alphabet[alphabet.index(letter) - shift_amount]
    print(f"Here is the decoded result: {decrypted_text}")
            
def caesar(way, original_text, shift_number):
    if way == "encode":
        encrypt(original_text, shift_number)
    else:
        decrypt(original_text, shift_number)

caesar(direction,text, shift)
