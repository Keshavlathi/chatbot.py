from datetime import datetime, date  # Import at the top

def chatbot():
    print("Welcome to the Rule-Based Chatbot! Type 'exit' to quit.")
    while True:
        user_input = input("You: ").strip().lower()

        if user_input == 'exit':
            print("Chatbot: Goodbye!")
            break

        elif 'hello' in user_input or 'hi' in user_input:
            print("Chatbot: Hello! How can I help you today?")

        elif 'how are you' in user_input:
            print("Chatbot: I'm just a bot, but I'm doing well! How about you?")

        elif 'your name' in user_input:
            print("Chatbot: My name is GitHub Copilot.")

        elif 'help' in user_input:
            print("Chatbot: Sure! Please tell me what you need assistance with.")

        elif 'time' in user_input:
            current_time = datetime.now().strftime('%H:%M:%S')
            print(f"Chatbot: The current time is {current_time}.")

        elif 'date' in user_input:
            today = date.today()
            print(f"Chatbot: Today's date is {today}.")

        elif 'weather' in user_input:
            print("Chatbot: I can't check live weather yet, but you can check your local forecast online!")

        elif 'joke' in user_input:
            print("Chatbot: Why did the computer go to the doctor? Because it caught a virus! ")

        elif 'thank you' in user_input or 'thanks' in user_input:
            print("Chatbot: You're welcome! ")

        else:
            print("Chatbot: Sorry, I didn't understand that. Can you please rephrase?")

if __name__ == "__main__":
    chatbot()
