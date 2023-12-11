"""Tests with librispeech dataset
"""
from pathlib import Path

import pytest

from audio_app.transcribe import transcribe


SAMPLES = [
    (
        Path(__file__).parents[2] / "data/test_sample.wav",
        "Okay, that's it. I quit. This guy's terrible."
    )
]


@pytest.mark.parametrize("file_name, text", SAMPLES)
def test_stt(file_name: Path, text: str):
    """Tests single file with no punctuation

    Transcribes file and checks that the transcription is correct
    (lowwercase, punctuation is not nesssary)

    Args:
        file_name: audio file
        file_name: correct transcription
    """
    transcription = transcribe(file_name)
    assert transcription["text"].strip().lower() == text.strip().lower()
