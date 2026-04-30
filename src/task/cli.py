import argparse

from task.settings import clear


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()

    return parser


def run() -> None:
    clear()  # limpa o terminal
    parser = build_parser()

    args = parser.parse_args()
    print(args)


if __name__ == "__main__":
    # entry point ao usar o módulo diretamente
    run()
