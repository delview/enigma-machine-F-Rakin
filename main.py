# F.Rakin_Enigma_Machine

# Chosen cipher : Ceaser Cipher 

# Either call a function to encrypt or to decrypt the string.

# Create two functions that will accept parameters in the form of a list or a dictionary that will contain the string meant to be encrypted or decrypted. 
def encrypter(message: list, shift_value: int) -> str:
    """
    This function encrypts the message into a secret code 
    """
    possible_inputs = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
                  "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", " ", "`", "~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+"
                  "[", "]", "|", "{", "}", "'", ";", ":", ",", ".", "/", "<", ">", "?"]
    
    encoded_list = []

    for old_letter in message:

        if old_letter in possible_inputs:
            old_index = possible_inputs.index(old_letter)
            new_index = (old_index + shift_value)  % len(possible_inputs) # returns the remainder using "%" modulus operator which loops back to the start of the list
            encoded_list.append(possible_inputs[new_index])
            
        else:
            print("Not a valid input!")
            option()
            
    encrypted_message = "".join(encoded_list)

    print(encrypted_message)


def decrypter(secret_message: list, shift_value: int) -> str:
    """
    This function decrypts the secret code into a message
    """
    possible_inputs = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
                "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", " ", "`", "~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+"
                "[", "]", "|", "{", "}", "'", ";", ":", ",", ".", "/", "<", ">", "?"]
    
    decoded_list = []

    for letter in secret_message:
        if letter in possible_inputs:
            old_index = possible_inputs.index(letter)
            new_index = (old_index - shift_value) % len(possible_inputs)
            decoded_list.append(possible_inputs[new_index])

        else:
            print("Invalid!")
            option()
    decrypted_message = "".join(decoded_list)
    
    print(decrypted_message)


# One function will encrypt while the other will decrypt using the cipher technique you have chosen. 

# This should involve both loops and if statements.

# Present the final encrypted or decrypted string to the user. 

# The user must be able to copy that output and run it through the program again to perfectly encrypt or decrypt it multiple times without any mistakes

# Create a program that will start by asking the user whether they want to decrypt or encrypt a message.
def option():
    """
    This function gives the user the option to encrypt or decrypt a message and then asks for the message. 
    """
    while True:
        try:
            choice = input("Please choose to encrypt or decrypt a message [e/d] : ").strip().lower()

            # Accept a string that the program will either encrypt or decrypt.
            message = input("\nWhat is your secret message? [No quotation marks!]: ").strip().lower()

            shift_value = int(input("Please enter a shift value [Same shift value needed to decrypt messages!]: "))
            
            # Call the encrypter function to encrypt the message
            if choice == "e":
                encrypter(message, shift_value)
                continue

            # Call th decrypter function to decrypt the message
            elif choice == "d":
                decrypter(message, shift_value)
                break

            # Continue the loop if a valid choice is not entered
            else: 
                print("Please enter [e/d] ")
                continue
            
        
        except ValueError:
            print("Please input a valid arguements! ")
            continue

if __name__ == "__main__":
    option()