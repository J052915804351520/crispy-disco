import logging
import os
import random
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

logging.basicConfig(level=logging.DEBUG)

# Safe: Loaded from environment configurations instead of hardcoded keys
BOT_TOKEN = os.environ.get("SLACK_BOT_TOKEN")
APP_TOKEN = os.environ.get("SLACK_APP_TOKEN")

app = App(token=BOT_TOKEN)

# 1. Public Dice Roll Command
@app.command("/roll-a-dice")
def dice_command(ack, respond, command):
    ack()
    roll = random.randint(1, 6)
    respond({
        "response_type": "in_channel",
        "text": f"🎲 <@{command['user_id']}> rolled a {roll}!"
    })

# 2. Public Coin Flip Command
@app.command("/flip-a-coin")
def flip_command(ack, respond, command):
    ack()
    result = random.choice(["Heads", "Tails"])
    respond({
        "response_type": "in_channel",
        "text": f"🪙 <@{command['user_id']}> flipped a coin and got **{result}**!"
    })

# 3. Public Magic 8-Ball Command
@app.command("/magic-8-ball")
def ball_command(ack, respond, command):
    ack()
    responses = [
        "It is certain.", "It is decidedly so.", "Without a doubt.",
        "Yes definitely.", "You may rely on it.", "As I see it, yes.",
        "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.",
        "Reply hazy, try again.", "Ask again later.", "Better not tell you now.",
        "Cannot predict now.", "Concentrate and ask again.", "Don't count on it.",
        "My reply is no.", "My sources say no.", "Outlook not so good.", "Very doubtful."
    ]
    answer = random.choice(responses)
    question = command.get('text', 'a question')
    respond({
        "response_type": "in_channel",
        "text": f"🔮 <@{command['user_id']}> asked: *\"{question}\"* \n🎱 Magic 8-Ball says: **{answer}**"
    })

if __name__ == "__main__":
    handler = SocketModeHandler(app, APP_TOKEN)
    handler.start()

