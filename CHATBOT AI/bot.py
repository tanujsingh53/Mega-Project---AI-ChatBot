import pyautogui
import time
import pyperclip
from openai import OpenAI
import keyboard


client = OpenAI(
  api_key="<Your-API-Key>",
)

try:
    import keyboard
    KEYBOARD_AVAILABLE = True
except ImportError:
    KEYBOARD_AVAILABLE = False
    print("[Info] 'keyboard' package not found. Ctrl+Alt+Q abort won't work unless you install it.")

def is_last_message_from_sender(chat_log, sender_name="Voda"):
  
    # Split the chat log into individyal messages
    messages = chat_log.strip().split("/2025 ]")[-1]
    if sender_name in messages:
       return True
    return False

pyautogui.FAILSAFE = True   # Move mouse to top-left to abort
ABORT_HOTKEY = "ESC" # Our custom abort combo
STOP = {"flag": False}

def _abort():
    STOP["flag"] = True
    print("\n[Abort] Hotkey pressed. Stopping actions…")

# Register hotkey in a background thread
if KEYBOARD_AVAILABLE:
    keyboard.add_hotkey(ABORT_HOTKEY, _abort)





    # Step 1: Click on the whatsapp icon at coordinates (1127, 1045)
pyautogui.click( 1236, 1048)
time.sleep(2)  # wait a bit

while True:
          

    # # Small delay before starting (so you can switch windows if needed)
    # time.sleep(2)

    

    # Step 2: Drag the mouse from (550, 145) to (1892, 936) to select the text
    pyautogui.moveTo(680,209)
    pyautogui.dragTo(944, 899, duration=2.0, button='left') # Drag for 1 second

    # time.sleep(0.5)

    # Step 3: Copy selected text (Ctrl+C) to the clipboard
    pyautogui.hotkey("ctrl", "c")
    pyautogui.click(1135, 916 )
    time.sleep(2)

    # Step 4: Get text from clipboard
    chat_history = pyperclip.paste()

    print(chat_history)
    print(is_last_message_from_sender(chat_history))
    if is_last_message_from_sender(chat_history):
      completion = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
          {"role": "system", "content": "You are a person named <Your Name> who speaks hindi as well as english. You are from India and you are a coder. You anaylze chat history and respond like <Your Name>. Output should be the next chat response as (text message only)"},
          {"role": "user", "content": chat_history}
      ]
      )

      response = completion.choices[0].message.content
      pyperclip.copy(response)  


      # Step 5: Click at (836, 971)
      pyautogui.click(836, 971)
      time.sleep(1)

      # Step 6: Paste the text
      pyautogui.hotkey("ctrl", "v")
      time.sleep(1)

      # Step 7: Press Enter
      pyautogui.press("enter")

