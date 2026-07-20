import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

# Initializes your app with your bot token
app = App(token=os.environ.get("SLACK_BOT_TOKEN"))

# Simple test command: responds when someone says "hello"
@app.message("hello")
def message_hello(message, say):
    say(f"Hey there <@{message['user']}>!")

if __name__ == "__main__":
    # Starts your app in Socket Mode so it listens forever
    handler = SocketModeHandler(app, os.environ.get("SLACK_APP_TOKEN"))
    handler.start()

