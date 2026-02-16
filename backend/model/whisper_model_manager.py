from model.interface.asr_model_manager import ASRModelManager
import whisper
from whisper import Whisper
from torch.cuda import is_available
from enum import Enum


class WhisperModelManager(ASRModelManager):

    def __init__(
        self,
        model_size: str,
        device: str | None = None
    ) -> None:
        super().__init__()
        self.model: Whisper | None = None
        self.model_size: str = model_size
        self.device: str = 'cuda' if not device and is_available() else 'cpu'

    def load_model(self) -> None:
        self.model = whisper.load_model(
            name=self.model_size,
            device=self.device
        )

    def unload_model(self) -> None:
        del self.model
        self.model = None

    def transcribe(self, audio: str, file_format: str) -> str:
        if not self.model:
            self.load_model()
        if self.model:
            asr_result = self.model.transcribe(audio=audio)
        return ''
