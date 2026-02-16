from abc import ABC, abstractmethod


class ASRModelManager(ABC):

    @abstractmethod
    def load_model(self) -> None:
        ...

    @abstractmethod
    def unload_model(self) -> None:
        ...

    @abstractmethod
    def transcribe(self, audio: str, output_format: str) -> str:
        ...
