"""Приложение для работы с аудио
"""
from argparse import ArgumentParser
from pathlib import Path
import json

from audio_app.modify import modify
from audio_app.transcribe import transcribe


def main():
    parser = ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(
        dest="subparsers")

    modify_parser = subparsers.add_parser(
        "modify", help="Модифицировать аудио")
    modify_parser.add_argument(
        "--file", "-f", type=Path,
        required=True, help="Путь к файлу")
    modify_parser.add_argument(
        "--output", "-o", type=Path,
        required=True, help="Путь к сохраняемому файлу"
    )
    modify_parser.add_argument(
        "--speed", type=float, default=1.0,
        help="Во сколько раз нужно изменить скорость аудио"
    )
    modify_parser.add_argument(
        "--volume", type=float, default=1.0,
        help="Во сколько раз нужно изменить громкость аудио"
    )
    modify_parser.add_argument(
        "--verbose", default=False, action="store_true",
        help="Нужно ли выводить в консоль информацию о результатах"
    )

    transcribe_parser = subparsers.add_parser(
        "transcribe", help="Перевести аудио в текст")
    transcribe_parser.add_argument(
        "--file", "-f", type=Path,
        required=True, help="Путь к файлу"
    )
    transcribe_parser.add_argument(
        "--output", "-o", type=Path,
        required=True, help="Путь к сохраняемому файлу"
    )
    transcribe_parser.add_argument(
        "--verbose", default=False, action="store_true",
        help="Нужно ли выводить в консоль информацию о результатах"
    )

    args = parser.parse_args()

    if args.subparsers == "modify":
        modify(args.file, args.output, args.speed, args.volume)

    elif args.subparsers == "transcribe":
        result = transcribe(args.file)
        if args.verbose:
            print(result)
        with open(args.output, "w", encoding="utf-8") as f:
            json.dump(result, f)


if __name__ == "__main__":
    main()
