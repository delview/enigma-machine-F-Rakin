
# Make a list called "messages" containing a series of short text messages. 
messages = ["Hello!", "Hi!", "What are you doing?", "I am happy."]

# Pass the list to a function called "show_messages()"
def show_messages(messages: list) -> str:
    """
    This function prints out each text message in the list
    """
    # Print out each text message individually
    for message in messages:
        print(message)

# Call function to run the program
if __name__ == "__main__":
    show_messages(messages)