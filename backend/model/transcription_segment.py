class TranscriptionSegment:

    def __init__(
        self,
        start: float,
        end: float,
        text: str
    ) -> None:
        self.start: float = start
        self.end = end
        self.text = text
