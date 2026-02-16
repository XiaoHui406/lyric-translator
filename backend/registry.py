from model.asr_output_formatter import ASROutputFormatter
from model.interface.asr_model_manager import ASRModelManager
from model.whisper_model_manager import WhisperModelManager

asr_output_formatter: ASROutputFormatter = ASROutputFormatter()

asr_model_manager: ASRModelManager = WhisperModelManager('small')
