import requests
import time

# Your Telegram Bot Token and Chat ID
TELEGRAM_TOKEN = "7921295854:AAG1eJ2sIEyRZxQRsrCeDvcbFFK1QTEYzyM"
CHAT_ID = "6591377041"

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
    # Static example – this will be replaced with real data from API later
    return [
        {
            "league": "Premier League",
            "home": "Manchester City",
            "away": "Chelsea",
            "odds": "1.65 - 4.20 - 5.00",
            "prediction": "Over 2.5 Goals"
        },
        {
            "league": "La Liga",
            "home": "Barcelona",
            "away": "Real Betis",
            "odds": "1.80 - 3.80 - 4.60",
            "prediction": "BTTS"
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
        time.sleep(3600)  # Wait 1 hour before sending again

if __name__ == "__main__":
    run_bot()
