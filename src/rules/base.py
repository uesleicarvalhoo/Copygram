import re
from abc import abstractclassmethod
from typing import Dict


class BaseSignal:
    coin: str = None
    entry: str = None
    signal: str = None
    expiration: str = None
    __base_message: str = None

    @abstractclassmethod
    def parse_message(self, message: str):
        raise NotImplementedError("Method parse_message must be implemented!")

    @abstractclassmethod
    def validate_message(self, message: str) -> bool:
        raise NotImplementedError("Method validated_message must be implemented!")

    def filter_signal(self, signal: str):
        signal = self.__remove_emoji(signal)
        signal = re.sub('ACIMA', 'CALL', signal)
        signal = re.sub('ABAIXO', 'PUT', signal)

        return signal

    def validate_signal(self) -> bool:
        return self.coin and self.expiration and self.entry and self.signal

    def __remove_emoji(self, string: str) -> str:
        emoji_pattern = re.compile(
            "["
            u"\U0001F600-\U0001F64F"  # emoticons
            u"\U0001F300-\U0001F5FF"  # symbols & pictographs
            u"\U0001F680-\U0001F6FF"  # transport & map symbols
            u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
            u"\U00002702-\U000027B0"
            u"\U000024C2-\U0001F251"
            "]+",
            flags=re.UNICODE,
        )

        return emoji_pattern.sub(r'', string)

    @property
    def base_message(self) -> str:
        return (
            f"💵 Moeda:                      {self.coin}",
            f"\n⏳ Expiração da vela:   {self.expiration}",
            f"\n⏰ Entrada:                   {self.entry}",
            f"\n🚦 Sinal:                         {self.signal}",
        )

    @property
    def channels_messages(self) -> Dict:
        raise NotImplementedError('Property "channels_message" must be implemented!')
