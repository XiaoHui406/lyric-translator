from fastapi import FastAPI, UploadFile
import uvicorn
import whisper
from whisper import Whisper
from whisper.utils import get_writer
import shutil
import os
from registry import asr_model_manager

app = FastAPI()

model: Whisper | None = None


@app.get("/load_asr_model/{model_name}")
def load_asr_model(model_name: str) -> str:
    model = whisper.load_model(model_name)
    lyric = model.transcribe('')
    writer = lyric['']
    return "load asr model successed"


@app.post('/run_asr/{output_format}')
def run_asr(file: UploadFile, output_format: str) -> str:
    temp_file = f'audio/temp_{file.filename}'
    with open(temp_file, 'wb') as buffer:
        shutil.copyfileobj(file.file, buffer)

    result = asr_model_manager.transcribe(
        audio=temp_file,
        output_format=output_format
    )

    if os.path.exists(temp_file):
        os.remove(temp_file)

    return result


if __name__ == "__main__":
    uvicorn.run('main:app', reload=True)
