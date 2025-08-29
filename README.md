# Mega-Project---AI-ChatBot

his project demonstrates how to automate interactions with a chat interface (or any text input field) using Python’s PyAutoGUI. The script automatically:

Clicks on a given screen coordinate.

Selects text from a defined region.

Copies the selected text into a Python variable.

Clicks inside a chatbox.

Types the text from the variable directly (no clipboard required).

Sends the message by pressing Enter.

🚀 Features

Automated mouse control → click, drag, and select screen regions.

Clipboard handling → copy text into a Python variable for reuse.

Direct variable typing → send text without relying on clipboard (typewrite).

Custom coordinates → works with any app or chatbox (just update positions).

Lightweight → built only with pyautogui and pyperclip.

🛠️ Tech Stack

PyAutoGUI
 – Mouse/keyboard automation

Pyperclip
 – Clipboard text handling

Python 3.x

📂 Project Workflow
flowchart TD
    A[Click at target coordinate] --> B[Drag & select text region]
    B --> C[Copy text using Ctrl+C]
    C --> D[Store copied text in variable]
    D --> E[Click chatbox input]
    E --> F[Type variable content directly]
    F --> G[Press Enter to send]

📖 Example Usage
import pyautogui, time, pyperclip

time.sleep(2)  # delay to switch window

# Click & select
pyautogui.click(1127, 1045)
pyautogui.moveTo(550, 145)
pyautogui.dragTo(1892, 936, duration=1, button="left")

# Copy selection into variable
pyautogui.hotkey("ctrl", "c")
copied_text = pyperclip.paste()

# Paste into chatbox
pyautogui.click(836, 971)
pyautogui.typewrite(copied_text, interval=0.02)
pyautogui.press("enter")

🔧 Setup

Clone this repo:

git clone https://github.com/your-username/ai-chatbot-automation.git
cd ai-chatbot-automation


Install requirements:

pip install pyautogui pyperclip


Run the script:

python bot.py

💡 Motivation & Use Cases

This project is designed to simulate real user behavior when testing or interacting with chat-based systems. Some common use cases include:

🤖 AI Chatbot Testing – Automate inputs/outputs to test chatbot responses without manually typing.

💬 Messaging Apps Automation – Send messages on platforms like WhatsApp Desktop, Slack, or MS Teams automatically.

🧪 QA Automation – Validate that chatbots respond correctly to specific queries.

📑 Workflow Automation – Auto-copy data from one application and send it to another (like reporting tools).

🎯 Productivity Boost – Reduce repetitive tasks (typing the same commands or messages multiple times)
