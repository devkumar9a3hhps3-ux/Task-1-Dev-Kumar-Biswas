import time
import random

def clean_input(user_input):
    return user_input.lower().strip()

def typing_effect(text):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.02)
    print()

responses = {
    "greeting": {
        "keywords": ["hello", "hi", "hey", "good morning", "good evening"],
        "responses": [
            "Hello! How can I assist you today?",
            "Hi there! What can I do for you?",
            "Hey! Nice to talk to you!"
        ]
    },
    "how_are_you": {
        "keywords": ["how are you", "how are you doing"],
        "responses": [
            "I'm functioning perfectly!",
            "All systems running smoothly!",
            "Doing great! Thanks for asking."
        ]
    },
    "name": {
        "keywords": ["your name", "who are you"],
        "responses": [
            "I am your AI chatbot assistant.",
            "You can call me ChatBot!",
            "I'm a rule-based AI chatbot created in Python."
        ]
    },
    "help": {
        "keywords": ["help", "what can you do"],
        "responses": [
            "I can answer basic questions and chat with you!",
            "Try asking about AI, jokes, or greetings.",
            "I'm here to assist you with simple queries."
        ]
    },
    "about_ai": {
        "keywords": ["what is ai", "define ai"],
        "responses": [
            "AI stands for Artificial Intelligence.",
            "AI enables machines to mimic human intelligence.",
            "Artificial Intelligence allows systems to learn and make decisions."
        ]
    },
    "joke": {
        "keywords": ["joke", "tell me a joke"],
        "responses": [
            "Why did the computer get cold? Because it forgot to close Windows!",
            "Why do programmers prefer dark mode? Because light attracts bugs!",
            "Why did the developer go broke? Because he used up all his cache!"
        ]
    },
    "time": {
        "keywords": ["time", "current time"],
        "responses": [
            f"The current time is {time.strftime('%H:%M:%S')}"
        ]
    },
    "date": {
        "keywords": ["date", "today"],
        "responses": [
            f"Today's date is {time.strftime('%Y-%m-%d')}"
        ]
    },
    "thanks": {
        "keywords": ["thank you", "thanks"],
        "responses": [
            "You're welcome!",
            "Happy to help!",
            "Anytime 😊"
        ]
    },
    "creator": {
        "keywords": ["who made you", "creator"],
        "responses": [
            "I was created as part of an AI internship project.",
            "A developer built me using Python.",
            "I was designed for learning AI fundamentals."
        ]
    },
    "weather": {
        "keywords": ["weather"],
        "responses": [
            "I can't check real-time weather yet, but it's always a good day to code!",
            "Weather APIs coming soon 😄"
        ]
    },
    "motivation": {
        "keywords": ["motivate me", "motivation"],
        "responses": [
            "Keep going, you're doing great!",
            "Every expert was once a beginner.",
            "Consistency is the key to success."
        ]
    },
    "bye": {
        "keywords": ["bye", "goodbye"],
        "responses": [
            "Goodbye! Have a great day!",
            "See you later!",
            "Take care!"
        ]
    }
}

def get_response(user_input):
    for intent in responses.values():
        for keyword in intent["keywords"]:
            if keyword in user_input:
                return random.choice(intent["responses"])
    return random.choice([
        "I'm not sure I understand. Can you rephrase?",
        "Sorry, I didn't get that.",
        "Try asking something else!"
    ])

def chatbot():
    print("AI Chatbot Initialized! (type 'exit' to quit)\n")
    while True:
        user_input = input("You: ")
        cleaned = clean_input(user_input)

        if cleaned == "exit":
            typing_effect("Bot: Exiting chatbot. Goodbye!")
            break

        response = get_response(cleaned)
        typing_effect("Bot: " + response)

if __name__ == "__main__":
    chatbot()