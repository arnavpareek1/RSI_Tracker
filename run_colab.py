import requests
import os

# Your Colab Notebook ID
NOTEBOOK_ID = "1z-QojWO6_bEdsZVeZBVfBVrn9LGHkIe_#scrollTo=pJzbof-3_biH"

# Telegram Bot Setup (Optional)
TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

def send_telegram_message(message):
    if TELEGRAM_TOKEN and CHAT_ID:
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        payload = {"chat_id": CHAT_ID, "text": message}
        requests.post(url, json=payload)

def trigger_colab():
    colab_url = f"https://colab.research.google.com/drive/{NOTEBOOK_ID}"
    response = requests.get(colab_url)
    
    if response.status_code == 200:
        send_telegram_message("🚀 Colab Notebook Execution Started at 9 AM!")
    else:
        send_telegram_message("❌ Failed to trigger Colab Notebook.")
    
if __name__ == "__main__":
    trigger_colab()
