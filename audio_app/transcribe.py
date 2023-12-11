"""Скрипт для расшифровки аудиофайла
"""
from pathlib import Path

import torch
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline

# TODO: auto device id detection
device = "cuda:0" if torch.cuda.is_available() else "cpu"
torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32


def transcribe(
        file_name: Path) -> dict[str, str]:
    model_name = "openai/whisper-large-v3"
    model = AutoModelForSpeechSeq2Seq.from_pretrained(
        model_name,
        torch_dtype=torch_dtype,
        low_cpu_mem_usage=True, use_safetensors=True
    )
    model.to(device)

    processor = AutoProcessor.from_pretrained(model_name)

    pipe = pipeline(
        "automatic-speech-recognition",
        model=model,
        tokenizer=processor.tokenizer,
        feature_extractor=processor.feature_extractor,
        max_new_tokens=128,
        chunk_length_s=30,
        batch_size=16,
        return_timestamps=False,
        torch_dtype=torch_dtype,
        device=device)

    result = pipe(str(file_name))
    result["file_name"] = file_name.name

    return result
