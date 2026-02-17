from fastapi import FastAPI, UploadFile
import uvicorn
import shutil
import os
from typing import List
from registry import asr_model_manager
from model.transcription_segment import TranscriptionSegment

app = FastAPI()


@app.get("/load_asr_model/{model_name}")
def load_asr_model(model_name: str) -> str:
    asr_model_manager.load_model()
    return "load asr model successed"


@app.post('/run_asr/{output_format}')
def run_asr(file: UploadFile, output_format: str) -> List[TranscriptionSegment]:
    temp_file = f'audio/temp_{file.filename}'
    with open(temp_file, 'wb') as buffer:
        shutil.copyfileobj(file.file, buffer)

    result: List[TranscriptionSegment] = asr_model_manager.transcribe(
        audio=temp_file,
        output_format=output_format
    )

    if os.path.exists(temp_file):
        os.remove(temp_file)

    return result


if __name__ == "__main__":
    uvicorn.run('main:app', reload=True)
