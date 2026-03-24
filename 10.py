# Create a simple Chabot that answers user questions using a predefined set of responses on keywords.

def chatbot_response(user_input):
    user_input = user_input.lower()
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"
    elif "name" in user_input:
        return "I am a simple chatbot."
    elif "how are you" in user_input:
        return "I am doing well. Thank you for asking!"
    elif "python" in user_input:
        return "Python is a popular programming language."
    elif "help" in user_input:
        return "I can answer simple questions based on keywords."
    elif "bye" in user_input or "exit" in user_input:
        return "Goodbye! Have a nice day."
    else:
        return "Sorry, I don't understand that."
print("Chatbot: Hello! Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    response = chatbot_response(user_input)
    print("Chatbot:", response)
    if "bye" in user_input.lower() or "exit" in user_input.lower():
        break