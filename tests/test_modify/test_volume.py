"""Тесты для модификации громкости аудиофайла
"""
from pathlib import Path
import tempfile

import torchaudio
import pytest

from audio_app.modify import modify


@pytest.mark.parametrize("value", [0.0, 0.5, 1.0, 1.5, 2.0])
def test_volume_value(value: float):
    """Tests change volume of audio file

    Increces audio_file volume by given value
    and checks if new volume of output file is correct.

    Args:
        value: value to change volume
    """
    file_name = Path(__file__).parents[2] / "data/test_sample.wav"
    output_name = Path(tempfile.mkdtemp()) / "test_sample_modified.wav"

    modify(file_name, output_name, 1, value)

    waveform, _ = torchaudio.load(file_name)
    new_waveform, _ = torchaudio.load(output_name)

    # Check duration is same
    assert waveform.shape[0] == new_waveform.shape[0]
    # Check volume is changed
    # NOTE: not very representative test
    assert (waveform * 2 - new_waveform).sum() < 0.5


def test_negative_volume():
    """Tests change volume of audio file

    Tries to change audio_file volume by negative value
    Catches ValueError exception.
    """
    file_name = Path(__file__).parents[2] / "data/test_sample.wav"
    output_name = Path(tempfile.mkdtemp()) / "test_sample_modified.wav"

    with pytest.raises(ValueError):
        modify(file_name, output_name, 1, -1)
