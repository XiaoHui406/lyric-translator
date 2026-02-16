from abc import ABC, abstractmethod


class ASRModelManager(ABC):

    @abstractmethod
    def load_model(self) -> None:
        ...

    @abstractmethod
    def unload_model(self) -> None:
        ...

    @abstractmethod
    def transcribe(self, audio: str, file_format: str) -> str:
        ...
