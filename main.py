# F.Rakin_Enigma_Machine

# Chosen cipher : Ceaser Cipher 

# Function to greet the user
def greeting() -> str :
    """
    This function asks the user's name and greets the user
    """
    name = input("What is your name? \n").title().strip()

    print(f"Hi {name}! Welcome to my Enigma Machine.") 


# Function that will accept parameters in the form of a list or a dictionary that will contain the string meant to be encrypted
def encrypter(possible_inputs: list, message: list, shift_value: int) -> str:
    """
    This function encrypts the message into a secret code 
    """
    # Empty list to store encrypted letters
    encoded_list = []

    # Loop through all the letters in the inputted message
    for old_letter in message:
        
        if old_letter in possible_inputs:

            # If the letter is in the list of possible inputs, find its index
            old_index = possible_inputs.index(old_letter)

            # Add shift value to the index
            # Return the remainder using "%" modulus operator which loops back to the start of the list
            new_index = (old_index + shift_value)  % len(possible_inputs) 

            # Append the new letter to the list
            encoded_list.append(possible_inputs[new_index])
            
        # Print invalid statement if unknown characters are entered
        else:
            print("Not a valid input!")

            # Run the main program from start again
            option()
            
    # Convert the list to a string and store it in a variable 
    encrypted_message = "".join(encoded_list)

    # Display the encrypted message
    print(f"Your secret message is : {encrypted_message}")


# Function that will accept parameters in the form of a list or a dictionary that will contain the string meant to be decrypted
def decrypter(possible_inputs: list, secret_message: list, shift_value: int) -> str:
    """
    This function decrypts the secret code into a message
    """
    # Empty list to store the decrypted letters
    decoded_list = []

    # Loop through each letter in the encrypted message
    for letter in secret_message:

        if letter in possible_inputs:
            # If the letter is in the list of possible inputs, find its index
            old_index = possible_inputs.index(letter)

            # Subtract shift value from the index
            # Return the remainder using "%" modulus operator which loops back to the start of the list
            new_index = (old_index - shift_value) % len(possible_inputs)

            # Append the decrypted letters into the list
            decoded_list.append(possible_inputs[new_index])

        # Print invalid statement if unknown characters are entered
        else:
            print("Invalid!")

            # Run the main program again
            option()

    # Convert the list to a string and store it in a variable 
    decrypted_message = "".join(decoded_list)
    
    # Display the decrypted message
    print(f"\nOh no! Secrets out.\tThe original message was : {decrypted_message}")


# Main function that is called to ask for inputs
def option():
    """
    This function gives the user the option to encrypt or decrypt a message and then asks for the message. 
    """
    # List of all possible inputs from the user
    possible_inputs = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", 
        "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
        "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", " ", "`", "~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+",
        "[", "]", "|", "{", "}", "'", ";", ":", ",", ".", "/", "<", ">", "?"]

    while True:
        try:
            # Ask if the user wants to encrypt or decrypt 
            choice = input("\nPlease choose to encrypt or decrypt a message [e/d] : ").strip().lower()

            # Accept a string that the program will either encrypt or decrypt.
            message = input("\nWhat is your secret message? [No quotation marks!]: ").strip()

            # Ask for a shift value for Caeser Cipher
            shift_value = int(input("\nPlease enter a shift value [Same shift value needed to decrypt messages!]: "))
            
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
            print("Please input valid integers! ")
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
            print("Thank you for using the Enigma Machine! ")
            break

        # Tell user to choose only between "y/n"
        else:
            print("Please enter y/n ") 


# Call the functions to run the program
if __name__ == "__main__":
    greeting()
    option()
    use_again()