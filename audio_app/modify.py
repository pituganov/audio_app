"""Скрипт для модификации аудиофайла
"""
from pathlib import Path

import torchaudio


def modify(file_name: Path, output_name: Path, speed: float, volume: float):
    """Изменяет громкость и скорость в аудофайле

    Args:
        file_name: название оригинального файла
        output_name: название измененного аудиофайла
        speed: во сколько раз нужно изменить скорость аудио
        volume: во сколько раз нужно изменить громкость аудио
    """
    if speed <= 0.0:
        raise ValueError("Скорость должна быть больше нуля")
    if volume < 0.0:
        raise ValueError("Громкость не может быть меньше нуля")

    waveform, sample_rate = torchaudio.load(file_name)

    # Изменяем громкость
    waveform = waveform * volume

    # Изменяем скорость
    waveform, _ = torchaudio.transforms.Speed(
        factor=speed, orig_freq=sample_rate)(waveform)

    # Сохраняем измененный аудиофайл
    torchaudio.save(output_name, waveform, sample_rate)
