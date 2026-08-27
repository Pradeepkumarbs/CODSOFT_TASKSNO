"""
CODSOFT AI Internship - Task 1
Rule-Based Chatbot with predefined responses.

Run:
    python chatbot.py
"""

import re
from datetime import datetime


RESPONSES = {
    "greeting": [
        "Hello! How can I help you today?",
        "Hi! Nice to meet you. What can I do for you?",
        "Hey! How may I assist you?"
    ],
    "name": [
        "I'm CodBot, a simple rule-based chatbot created for the CodSoft AI internship."
    ],
    "help": [
        "I can answer questions about my name, capabilities, internship tasks, and the current time. Try asking 'What can you do?'"
    ],
    "capabilities": [
        "I can respond to predefined user queries using keyword and pattern matching."
    ],
    "internship": [
        "The CodSoft Artificial Intelligence internship requires at least 3 tasks for successful completion."
    ],
    "task1": [
        "Task 1 is to build a simple chatbot that responds to user inputs based on predefined rules."
    ],
    "thanks": [
        "You're welcome!",
        "Happy to help!",
        "Anytime!"
    ],
    "goodbye": [
        "Goodbye! Best of luck with your AI internship!",
        "See you later! Keep learning and building."
    ]
}


def normalize(text):
    """Convert input to lowercase and remove unnecessary punctuation."""
    return re.sub(r"[^a-z0-9\s]", "", text.lower()).strip()


def get_response(user_input):
    """Match the normalized input against predefined rules."""
    text = normalize(user_input)

    if not text:
        return "Please type something so I can respond."

    if re.search(r"\b(hi|hello|hey|good morning|good afternoon|good evening)\b", text):
        return RESPONSES["greeting"][0]

    if re.search(r"\b(your name|who are you|what are you)\b", text):
        return RESPONSES["name"][0]

    if re.search(r"\b(help|how can you help)\b", text):
        return RESPONSES["help"][0]

    if re.search(r"\b(what can you do|capabilities|features)\b", text):
        return RESPONSES["capabilities"][0]

    if re.search(r"\b(internship|codsoft)\b", text):
        return RESPONSES["internship"][0]

    if re.search(r"\b(task 1|task one|chatbot)\b", text):
        return RESPONSES["task1"][0]

    if re.search(r"\b(thanks|thank you|thankyou)\b", text):
        return RESPONSES["thanks"][0]

    if re.search(r"\b(time|current time)\b", text):
        return f"The current time is {datetime.now().strftime('%I:%M %p')}."

    if re.search(r"\b(bye|goodbye|exit|quit)\b", text):
        return RESPONSES["goodbye"][0]

    return (
        "I'm sorry, I don't understand that yet. "
        "Try asking about my name, capabilities, the internship, Task 1, or the current time."
    )


def main():
    print("=" * 60)
    print("                 CODBOT - RULE-BASED CHATBOT")
    print("=" * 60)
    print("Type 'bye' or 'exit' to end the conversation.\n")

    while True:
        user_input = input("You: ")
        response = get_response(user_input)
        print(f"CodBot: {response}\n")

        if re.search(r"\b(bye|goodbye|exit|quit)\b", normalize(user_input)):
            break


if __name__ == "__main__":
    main()
