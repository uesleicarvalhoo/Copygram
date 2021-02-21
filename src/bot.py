import logging
import re

from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.types import PeerChannel

from src.settings import API_HASH, API_TOKEN, TELEGRAM_STRING_SESSION
from src.utils import load_signal

client = TelegramClient(StringSession(TELEGRAM_STRING_SESSION), API_TOKEN, API_HASH)


@client.on(events.NewMessage())
async def handler_new_message(event):
    logging.info("New message: %s" % event.message.message)
    channel_id = get_channel_id_from_peer(str(event.message.to_id))

    signal = load_signal(channel_id)
    event_message = event.message.message

    if not signal or not signal.validate_message(event_message):
        return

    signal.parse_message(event_message)

    if not signal.validate_signal():
        return

    for channel_id, message in signal.channels_messages.items():
        logging.info("Signal validated, sending message to Channel %s.." % channel_id)
        channel = await client.get_entity(PeerChannel(channel_id))

        await client.send_message(
            entity=channel,
            message=message,
        )


def get_channel_id_from_peer(peer: str) -> str:
    return re.findall(r'\b\d+\b', peer)[0]


logging.basicConfig(level=logging.INFO, format="[%(asctime)s] %(levelname)s: %(message)s", datefmt="%d-%m-%Y %H-%M-%S")

if __name__ == '__main__':
    client.start()
    client.run_until_disconnected()
