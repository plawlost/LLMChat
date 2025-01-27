from discord import User, Client
from llmchat.config import Config
from llmchat.persistence import PersistentData
import io

class TTSSource:
    def __init__(self, client: Client, config: Config, db: PersistentData):
        self.config = config
        self.db = db
        self.client = client

    # Returns the raw audio bytes
    async def generate_speech(self, content: str) -> io.BufferedIOBase:
        return NotImplementedError()

    def list_voices(self) -> list[str]:
        return NotImplementedError()

    def set_voice(self, voice_id: str) -> None:
        return NotImplementedError()

    @staticmethod
    def _add_silence(buf: io.BufferedIOBase, seconds_of_silence: int) -> io.BufferedIOBase:
        pass

    @property
    def current_voice_name(self) -> str:
        return "Unknown voice"
