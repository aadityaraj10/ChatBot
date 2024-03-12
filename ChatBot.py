


import tkinter
m = tkinter.Tk()
'''
widgets are added here
'''



def simple_chatbot(user_input):
    # Convert user input to lowercase for case-insensitive matching
    user_input = user_input.lower()

    # Define predefined rules and responses
    rules_responses = {
        "hello": "Hello! How can I help you?",
        "how are you": "I'm just a computer program, but I'm doing well. How about you?",
        "what is your name": "I'm a chatbot, you can call me CBT.",
        "bye": "Goodbye! If you have more questions, feel free to ask.",
        "age": "I don't have an age, as I'm just a program.",
        "what do you do": "I'm here to assist and answer your questions.",
        "help": "Sure, I'm here to help. What do you need assistance with?",
        "who created you": "I was created by Aaditya.",
        "weather": "I'm sorry, I don't have real-time information. You can check a weather website for updates.",
        "thanks": "You're welcome! If you have more questions, feel free to ask.",
    }

    # Check if user input matches any predefined rule
    for rule, response in rules_responses.items():
        if rule in user_input:
            return response

    # If no match is found, provide a default response
    return "I'm sorry, I didn't understand that. Can you please ask in a different way?"

# Take input from the user and get responses until the user says 'exit'
while True:
    user_input = input("You: ")
    
    # Check if the user wants to exit
    if user_input.lower() == 'exit':
        print("Chatbot: Goodbye!")
        break
    
    # Get the chatbot's response based on user input
    response = simple_chatbot(user_input)
    print("Chatbot:", response)

m.mainloop()