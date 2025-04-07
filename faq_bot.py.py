import difflib

# Define FAQ data
faq_data = {
    "What are your opening hours?": "We are open from 9 AM to 9 PM every day.",
    "Where are you located?": "We are located at 123 Main Street, Springfield.",
    "How can I book an appointment?": "You can book an appointment through our website or by calling us at 123-456-7890.",
    "Do you offer online consultations?": "Yes, we do offer online consultations via Zoom.",
    "What is your refund policy?": "Refunds are available within 14 days of purchase with a valid receipt."
}

# Function to match user input with the closest FAQ question
def match_question(user_input):
    questions = list(faq_data.keys())
    best_match = difflib.get_close_matches(user_input, questions, n=1, cutoff=0.5)
    if best_match:
        return faq_data[best_match[0]]
    else:
        return "Sorry, I couldn't find an answer to your question."

# Chat function to interact with the bot
def chat():
    print("🤖 Welcome to the FAQ Bot! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Bot: Goodbye! 👋")
            break
        answer = match_question(user_input)
        print("Bot:", answer)

# Run the chatbot
if __name__ == "__main__":
    chat()
