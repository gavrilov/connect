"""Server for sending direct message via telegram bot"""
import os
import requests
from flask import Flask, render_template, request, flash
from dotenv import load_dotenv


""" Load environment variables
    TELEGRAM_BOT_TOKEN: Telegram bot token
    TELEGRAM_CHAT_ID: Telegram chat id
    SECRET_KEY: Flask secret key
 """
load_dotenv()


def send_message(message):
    """Send message to telegram bot
    Args:
        message (str): message to send
    """
    url = f"https://api.telegram.org/bot{app.config['TELEGRAM_BOT_TOKEN']}/sendMessage"
    data = {"chat_id": app.config['TELEGRAM_CHAT_ID'], "text": message}
    r = requests.post(url, data=data)
    if r.status_code != 200:
        return False
    return True


app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")
app.config['TELEGRAM_BOT_TOKEN'] = os.getenv("TELEGRAM_BOT_TOKEN")
app.config['TELEGRAM_CHAT_ID'] = os.getenv("TELEGRAM_CHAT_ID")


@app.route("/", methods=['GET', 'POST'])
def main_page():
    """Main page - show form to send message to telegram bot or process form and show status"""
    if request.method == 'POST':
        name = request.form['name']
        message = request.form['message']
        if send_message(f"{name} says: {message}"):
            flash("Message sent successfully", 'success')
        else:
            flash("Unable to send message - please try again later", 'error')
    return render_template("send_message_form.html")


# run the app
if __name__ == "__main__":
    app.run(debug=True, port=8080, host='0.0.0.0')
