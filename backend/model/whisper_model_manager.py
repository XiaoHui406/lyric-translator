from model.interface.asr_model_manager import ASRModelManager
from model.transcription_segment import TranscriptionSegment
import whisper
from whisper import Whisper
from torch.cuda import is_available
from typing import List


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
        self.model: Whisper | None = None

    def transcribe(self, audio: str, output_format: str) -> List[TranscriptionSegment]:
        if not self.model:
            self.load_model()
        if self.model:
            segments: List[TranscriptionSegment] = []
            asr_result = self.model.transcribe(audio=audio)
            for item in asr_result['segments']:
                assert type(item) is dict
                segments.append(TranscriptionSegment(
                    start=item['start'],
                    end=item['end'],
                    text=item['text']
                ))
            return segments
        else:
            raise TypeError("model is None")
