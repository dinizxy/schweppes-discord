# main.py

from typing import Final
import os
from dotenv import load_dotenv
from responses import get_response
from discord import Intents, Client, Message, Embed
import re

# STEP 0: LOAD OUR TOKEN FROM SOMEWHERE SAFE
load_dotenv()
TOKEN: Final[str] = os.getenv("DISCORD_TOKEN")
print("TOKEN:", TOKEN)

# STEP 1: BOT SETUP
intents: Intents = Intents.default()
intents.message_content = True
client: Client = Client(intents=intents)

# STEP 2: MESSAGE FUNCTIONALITY


async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print("(Message was empty because intents were not enabled probably)")
        return

    is_private = user_message[0] == "?"
    if is_private:
        user_message = user_message[1:]

    try:
        # Check if the response is a URL
        if user_message.startswith("http://") or user_message.startswith("https://"):
            embed = Embed()
            embed.set_image(url=user_message)
            await message.channel.send(embed=embed)
        else:
            await message.channel.send(user_message)
    except Exception as e:
        print(e)


# STEP 3: HANDLING THE STARTUP FOR OUR BOT:
@client.event
async def on_ready() -> None:
    print(f"{client.user} is now running!")


# STEP 4: HANDLING INCOMING MESSAGES:
@client.event
async def on_message(message: Message) -> None:
    # Evita que o bot responda a si mesmo
    if message.author == client.user:
        return

    # Responde apenas se o bot for mencionado
    if client.user.mentioned_in(message):
        username: str = str(message.author)
        # Remove a menção do bot da mensagem para processar apenas o conteúdo restante
        user_message: str = re.sub(r'<@!?\d+>', '', message.content).strip()
        channel: str = str(message.channel)

        print(f'[{channel}] {username}: "{user_message}"')
        try:
            # Get the rule-based response
            response: str = get_response(user_message)
            await send_message(message, response)
        except Exception as e:
            print(f"Error during message processing: {e}")
            await message.channel.send("An error occurred while processing your message.")

# STEP 5 : MAIN ENTRY POINT:


def main() -> None:
    client.run(token=TOKEN)


if __name__ == "__main__":
    main()
