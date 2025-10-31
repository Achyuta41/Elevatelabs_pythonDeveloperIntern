def chatbot():
    print("🤖ChatBot: HI i'm chatbot.How can I help you today?")
    print("Type 'bye'to end the chat:\n")
    while True:
        user_input=input("You:").lower().strip()

        if user_input in ['hi','hello','hey']:
            print("🤖ChatBot: hello there! how are yoy today??")
        elif user_input in "how are you":
              print("🤖ChatBot: I am doing well , what about you?? 😊")
        elif "your name" in user_input:
               print("🤖ChatBot: I am just a virtual machine created by python")

        elif "bye" in user_input or "exit" in user_input:
            print("🤖ChatBot: Goodbye! have a great day")
            break
        else:
          print("🤖ChatBot: I am not sure how to respond to that. can you rephrase?")

if __name__=="__main__":
    chatbot()