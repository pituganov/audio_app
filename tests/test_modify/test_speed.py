"""Тесты для модификации скорости аудиофайла
"""
from pathlib import Path
import tempfile

import torchaudio
import pytest

from audio_app.modify import modify


file_name = Path(__file__).parents[2] / "data/test_sample.wav"


@pytest.mark.parametrize("value", [0.5, 1.0, 1.5, 2.0])
def test_speed_value(value: float):
    """Tests change speed of audio file

    Increces audio_file speed by given value
    and checks if new speed is correct.

    Args:
        value: speed value to change
    """
    file_name = Path(__file__).parents[2] / "data/test_sample.wav"
    output_name = Path(tempfile.mkdtemp()) / "test_sample_modified.wav"

    modify(file_name, output_name, value, 1)

    waveform, sr = torchaudio.load(file_name)
    new_waveform, _ = torchaudio.load(output_name)
    approx_diff = pytest.approx(
        waveform.shape[1] / new_waveform.shape[1],
        abs=0.001)

    assert waveform.shape[0] == new_waveform.shape[0]
    assert approx_diff == value


def test_negative_speed():
    """Tests change speed of audio file

    Tries to change audio_file speed by negative value
    Catches ValueError exception.
    """
    file_name = Path(__file__).parents[2] / "data/test_sample.wav"
    output_name = Path(tempfile.mkdtemp()) / "test_sample_modified.wav"

    with pytest.raises(ValueError):
        modify(file_name, output_name, -1, 1)
