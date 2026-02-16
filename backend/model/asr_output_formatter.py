from model.transcription_segment import TranscriptionSegment
from typing import List


class ASROutputFormatter():

    def format(
        self,
        output_format: str,
        segments: List[TranscriptionSegment]
    ) -> str:
        ...

    def _to_srt(
        self,
        segments: List[TranscriptionSegment]
    ) -> str:
        ...

    def _to_lrc(
        self,
        segments: List[TranscriptionSegment]
    ) -> str:
        ...

    def _to_txt(
        self,
        segments: List[TranscriptionSegment]
    ) -> str:
        ...

    def _to_json(
        self,
        segments: List[TranscriptionSegment]
    ) -> str:
        ...

    def _to_vtt(
        self,
        segments: List[TranscriptionSegment]
    ) -> str:
        ...

    def _to_tsv(
        self,
        segments: List[TranscriptionSegment]
    ) -> str:
        ...
