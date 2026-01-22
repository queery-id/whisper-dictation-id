"""
Text injection module - pastes transcribed text at cursor position
"""
import pyperclip
import keyboard
import time


def inject_text(text: str) -> bool:
    """Inject text at current cursor position using clipboard"""
    if not text:
        print("No text to inject")
        return False
    
    try:
        pyperclip.copy(text)
        time.sleep(0.05)
        keyboard.send('ctrl+v')
        time.sleep(0.1)
        print(f"Injected: \"{text[:50]}...\" " if len(text) > 50 else f"Injected: \"{text}\"")
        return True
    except Exception as e:
        print(f"Clipboard injection failed: {e}")
        try:
            keyboard.write(text, delay=0.01)
            return True
        except Exception as e2:
            print(f"Text injection failed: {e2}")
            return False
