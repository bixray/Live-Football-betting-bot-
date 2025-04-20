import requests
import time
import os

TELEGRAM_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
CHAT_ID = "YOUR_TELEGRAM_CHAT_ID"

def send_message(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": text,
        "parse_mode": "HTML"
    }
    try:
        requests.post(url, data=payload)
    except Exception as e:
        print("Error sending message:", e)

def get_match_data():
    # Placeholder example for match data (replace with actual API or source)
    return [
        {
            "league": "Premier League",
            "home": "Arsenal",
            "away": "Liverpool",
            "odds": "2.10 - 3.40 - 3.00",
            "prediction": "BTTS & Over 2.5"
        }
    ]

def run_bot():
    while True:
        matches = get_match_data()
        for match in matches:
            message = (
                f"<b>{match['league']}</b>\n"
                f"{match['home']} vs {match['away']}\n"
                f"<b>Odds:</b> {match['odds']}\n"
                f"<b>Prediction:</b> {match['prediction']}\n"
            )
            send_message(message)
        time.sleep(3600)  # Run hourly

if __name__ == "__main__":
    run_bot()
