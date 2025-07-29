import os
import time
import json
import pyttsx3
from dotenv import load_dotenv
from cryptography.fernet import Fernet

# === Load .env ===
load_dotenv(dotenv_path='./config/token.env')

# === Speech engine ===
speech_mode = True
use_ai_voice = True  # Change to False to use local robot voice

# === Secure passphrase ===
ENCRYPTION_KEY = os.getenv("ENCRYPTION_KEY")  # Must be a Fernet key
ENC_PASSPHRASE = os.getenv("ENC_PASSPHRASE")

if ENCRYPTION_KEY and ENC_PASSPHRASE:
    fernet = Fernet(ENCRYPTION_KEY)
    try:
        PASSPHRASE = fernet.decrypt(ENC_PASSPHRASE.encode()).decode()
    except Exception as e:
        PASSPHRASE = None
        print("[x] Failed to decrypt passphrase:", e)
else:
    PASSPHRASE = None

# === TTS speak function ===
def speak(text):
    if not speech_mode:
        return
    if use_ai_voice:
        try:
            import requests
            resemble_api_key = os.getenv("RESEMBLE_API_KEY")
            url = "https://app.resemble.ai/api/v2/projects/YOUR_PROJECT_ID/clips"
            headers = {
                "Authorization": f"Token {resemble_api_key}"
            }
            data = {
                "title": "AI Voice",
                "body": text,
                "voice_uuid": "YOUR_VOICE_ID"
            }
            res = requests.post(url, json=data, headers=headers)
            print("[Resemble] Sent:", text)
        except Exception as e:
            print("[!] Resemble AI error:", e)
    else:
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()

# === Log and speak ===
def log_and_speak(message):
    print(f"[+] {message}")
    speak(message)

# === Simulate background AI security process ===
def smart_voice_mining():
    log_and_speak("BinaryShield Voice Scanner Activated")
    while True:
        # Simulate detection
        time.sleep(15)
        log_and_speak("Monitoring biometric patterns...")
        # Simulate unlock
        if PASSPHRASE:
            log_and_speak("Wallet Unlocked")
        # Simulate threat
        log_and_speak("Intruder Detected")

if __name__ == "__main__":
    log_and_speak("BinaryShield AI running in voice-only mode")
    smart_voice_mining()