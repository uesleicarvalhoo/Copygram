from typing import Dict

from src.rules.base import BaseSignal
from src.settings import CHANNEL_ID_AO_VIVO, CHANNEL_ID_METODO_CONSISTENTE


class Signal(BaseSignal):
    def parse_message(self, message: str) -> str:
        new_message = []
        for text_line in message.replace("SIGNALS ELITE", "%(group_name)s").split("\n"):
            if not text_line:
                continue

            if "CH " in text_line:
                new_message.append("".join(text_line.split("CH ")))

            else:
                new_message.append(text_line)

        self.__base_message = "\n".join(new_message)

    def validate_signal(self) -> bool:
        return True

    @property
    def base_message(self) -> str:
        return self.__base_message

    def validate_message(self, message: str) -> bool:
        return "call" in message.lower() or "put" in message.lower()

    @property
    def channels_messages(self) -> Dict:
        return {
            CHANNEL_ID_AO_VIVO: self.base_message,
            CHANNEL_ID_METODO_CONSISTENTE: self.base_message,
        }
