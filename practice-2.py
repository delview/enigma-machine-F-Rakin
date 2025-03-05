
# Make a list called "messages" containing a series of short text messages. 
messages = ["Hello!", "Hi!", "What are you doing?", "I am happy."]

# Pass the list to a function called "show_messages()" which prints out each text message.
def show_messages(messages: list) -> str:
    """
    This function prints out each text message in the list
    """
    # Print out each text message individually
    for message in messages:
        print(message)


# Write a function called "send_messages()" that prints each text message and MOVES each message to a new list called "sent_messages" as it's printed. 
def send_messages(messages : list) -> str:
    """
    This function moves each text message to a new list and displays the list
    """
    # Start with an empty new list
    sent_messages = []

    # Loop through the list to print each element of the list seperately
    while messages:
        # Store the first message from the list in a variable before removing it from the list
        message = messages.pop(0)

        # Print the message
        print(message)

        # Move the message to a new list
        sent_messages.append(message)

    # Print the original list
    print(f"The original list : {messages}")

    # Print the new list
    print(f"The new list : {sent_messages}")


# After calling the function, print both of your lists to make sure the messages were moved correctly (there should be nothing left in the original list after it has been moved).
if __name__== "__main__":
    send_messages(messages)
