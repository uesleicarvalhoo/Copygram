from src.settings import CHANNEL_ID_METODO_CONSISTENTE
from typing import Dict

from src.rules.base import BaseSignal


class Signal(BaseSignal):
    def parse_message(self, message: str) -> None:
        self.__base_message = message.replace("Corujão 24hs", "%(group_name)s")

    def validate_signal(self) -> bool:
        return True

    @property
    def base_message(self) -> str:
        return self.__base_message

    def validate_message(self, message: str) -> bool:
        return True

    @property
    def channels_messages(self) -> Dict:
        return {CHANNEL_ID_METODO_CONSISTENTE: self.base_message % {"group_name": "Metodo Consistente"}}
