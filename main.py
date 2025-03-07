# F.Rakin_Enigma_Machine

# Chosen cipher : Ceaser Cipher 

# Function to greet the user
def greeting() -> str :
    """
    This function asks the user's name and greets the user
    """
    name = input("What is your name? \n").title().strip()

    print(f"Hi {name}! Welcome to my Number Guessing Game.") 


# Function that will accept parameters in the form of a list or a dictionary that will contain the string meant to be encrypted
def encrypter(possible_inputs: list, message: list, shift_value: int) -> str:
    """
    This function encrypts the message into a secret code 
    """
    # Store each new letter in an empty list
    encoded_list = []

    # Loop through all the letters in the inputted message
    for old_letter in message:
        

        if old_letter in possible_inputs:

            # If the letter is in the list of possible inputs, find its index
            old_index = possible_inputs.index(old_letter)

            # Add shift value to the index
            new_index = (old_index + shift_value)  % len(possible_inputs) # returns the remainder using "%" modulus operator which loops back to the start of the list
            encoded_list.append(possible_inputs[new_index])
            
        else:
            print("Not a valid input!")
            option()
            
    encrypted_message = "".join(encoded_list)

    print(encrypted_message)

# Function that will accept parameters in the form of a list or a dictionary that will contain the string meant to be decrypted
def decrypter(possible_inputs: list, secret_message: list, shift_value: int) -> str:
    """
    This function decrypts the secret code into a message
    """

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


def option():
    """
    This function gives the user the option to encrypt or decrypt a message and then asks for the message. 
    """
    # List of all possible inputs from the user
    possible_inputs = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
                "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", " ", "`", "~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+"
                "[", "]", "|", "{", "}", "'", ";", ":", ",", ".", "/", "<", ">", "?"]

    while True:
        try:
            # Ask if the user wants to encrypt or decrypt 
            choice = input("Please choose to encrypt or decrypt a message [e/d] : ").strip().lower()

            # Accept a string that the program will either encrypt or decrypt.
            message = input("\nWhat is your secret message? [No quotation marks!]: ").strip().lower()

            # Ask for a shift value for Caeser Cipher
            shift_value = int(input("Please enter a shift value [Same shift value needed to decrypt messages!]: "))
            
            # Call the encrypter function to encrypt the message
            if choice == "e":
                encrypter(possible_inputs, message, shift_value)
                continue

            # Call the decrypter function to decrypt the message
            elif choice == "d":
                decrypter(possible_inputs, message, shift_value)
                break

            # Continue the loop if a valid choice is not entered
            else: 
                print("Please enter [e/d] ")
                continue
            
        # Continue the loop  if invalid arguements are inputted
        except ValueError:
            print("Please input a valid arguements! ")
            continue

# Function to let the user use the Enigma Machine till they exit
def use_again() -> str:
    """
    This function gives the user the choice to use the Enigma Machine again
    """
    while True:

        # Ask if they want to use again, only accepting 'y' or 'n'
        choice = input("Do you wish to use the Enima Machine again? [y/n] - ").strip().lower()

        # Run option function again if user chooses "y"
        if choice == "y":
            option()

        # End the program if user chooses "n"    
        elif choice == "n":
            break

        # Tell user to choose only between "y/n"
        else:
            print("Please enter y/n ") 


if __name__ == "__main__":
    greeting()
    option()
    use_again()