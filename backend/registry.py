from manager.asr.interface.asr_model_manager import ASRModelManager
from manager.asr.whisper_model_manager import WhisperModelManager

asr_model_manager: ASRModelManager = WhisperModelManager('small')
