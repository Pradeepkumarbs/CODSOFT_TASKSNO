# CODSOFT AI Internship - Task 1
## Rule-Based Chatbot

### Objective
Build a simple chatbot that responds to user inputs based on predefined rules, using if-else statements and pattern matching.

### Technologies
- Python 3
- Regular expressions (`re`)
- `datetime` module

### Features
- Greeting detection
- Bot identity/name response
- Help and capabilities responses
- CodSoft internship information
- Task 1 information
- Thank-you response
- Current time response
- Goodbye/exit handling
- Fallback response for unknown queries

### Project Structure

```text
CODSOFT_TASK1_Rule_Based_Chatbot/
├── chatbot.py
├── README.md
└── requirements.txt
```

### How to Run

1. Install Python 3.
2. Open a terminal in this project folder.
3. Run:

```bash
python chatbot.py
```

No external packages are required.

### Example Conversation

```text
You: Hello
CodBot: Hello! How can I help you today?

You: What is your name?
CodBot: I'm CodBot, a simple rule-based chatbot created for the CodSoft AI internship.

You: What can you do?
CodBot: I can respond to predefined user queries using keyword and pattern matching.

You: Tell me about task 1
CodBot: Task 1 is to build a simple chatbot that responds to user inputs based on predefined rules.

You: bye
CodBot: Goodbye! Best of luck with your AI internship!
```

### How It Works

1. The user enters a message.
2. The message is normalized to lowercase and unnecessary punctuation is removed.
3. Regular-expression patterns check for known keywords and phrases.
4. The first matching rule produces a predefined response.
5. If no rule matches, the chatbot gives a fallback response.
6. The conversation continues until the user enters `bye`, `goodbye`, `exit`, or `quit`.

### Internship Requirement
The CodSoft AI internship document states that at least 3 tasks must be completed for successful completion. This repository contains Task 1.

### Future Improvements
- Add more conversation rules.
- Add a graphical user interface.
- Store conversation history.
- Add sentiment detection.
- Connect the bot to an NLP model for more flexible conversations.
