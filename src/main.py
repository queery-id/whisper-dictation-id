"""
Whisper Dictation - Main Entry Point
Press hotkey to toggle recording, transcribes and injects text.
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import keyboard
from audio_capture import AudioRecorder
from transcriber import transcribe, get_model
from text_injector import inject_text
from config import HOTKEY, MODEL_SIZE, USE_CLOUD


class WhisperDictation:
    def __init__(self):
        self.recorder = AudioRecorder()
        self.is_recording = False
        model_display = "Groq (large-v3)" if USE_CLOUD else MODEL_SIZE
        print("=" * 50)
        print("  WHISPER DICTATION - Indonesian")
        print("=" * 50)
        print(f"Hotkey: {HOTKEY.upper()}")
        print(f"Model: {model_display}")
        print("-" * 50)
    
    def preload_model(self):
        print("Pre-loading model...")
        get_model()
        print("-" * 50)
        print(f"Ready! Press {HOTKEY.upper()} to start speaking.")
        print(f"Press {HOTKEY.upper()} again to stop and transcribe.")
        print("Press Ctrl+C to exit.")
        print("-" * 50)
    
    def toggle_recording(self):
        if not self.is_recording:
            self.is_recording = True
            self.recorder.start()
        else:
            self.is_recording = False
            audio_path = self.recorder.stop()
            if audio_path:
                print("Transcribing...")
                text = transcribe(audio_path)
                if text:
                    inject_text(text)
                else:
                    print("No speech detected")
                try:
                    os.remove(audio_path)
                except:
                    pass
            print(f"\nReady. Press {HOTKEY.upper()} to record again.")
    
    def run(self):
        self.preload_model()
        keyboard.add_hotkey(HOTKEY, self.toggle_recording, suppress=True)
        try:
            keyboard.wait()
        except KeyboardInterrupt:
            print("\nGoodbye!")
            sys.exit(0)


def main():
    app = WhisperDictation()
    app.run()


if __name__ == "__main__":
    main()
