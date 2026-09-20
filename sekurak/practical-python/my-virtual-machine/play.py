#!/usr/bin/env python3
"""
pikVM - running melodies.

    python3 play.py cat                runs the melody
    python3 play.py cat --trace        shows step-by-step execution
    python3 play.py cat --disassemble  prints the bytecode as text
    python3 play.py cat --save         saves cat.wav
    python3 play.py                    lists available melodies
"""

import argparse
import importlib
import pathlib
import sys

from pikvm.assembler import disassemble
from pikvm.machine import Machine
from pikvm.sound import play, save_wav

MELODIES_DIR = pathlib.Path(__file__).parent / "melodies"


def available_melodies():
    return sorted(
        file.stem
        for file in MELODIES_DIR.glob("*.py")
        if not file.stem.startswith("_")
    )


def main():
    parser = argparse.ArgumentParser(
        description="A virtual machine that plays music.",
    )
    parser.add_argument(
        "melody", nargs="?", help="melody name from the melodies/ directory"
    )
    parser.add_argument(
        "--trace", action="store_true", help="show step-by-step execution"
    )
    parser.add_argument(
        "--disassemble", action="store_true", help="print the bytecode as text"
    )
    parser.add_argument(
        "--bytes", action="store_true", help="print the raw bytes"
    )
    parser.add_argument(
        "--save", action="store_true", help="save a .wav instead of just playing"
    )
    parser.add_argument(
        "--quiet", action="store_true", help="don't play any sound"
    )

    args = parser.parse_args()

    if args.melody is None:
        print("Available melodies:")
        for name in available_melodies():
            print(f"  {name}")
        print("\nUsage: python3 play.py <name>")
        return 0

    try:
        module = importlib.import_module(f"melodies.{args.melody}")
    except ModuleNotFoundError:
        print(f"No melody named '{args.melody}'.")
        print(f"Available: {', '.join(available_melodies())}")
        return 1

    program = module.program
    print(f"Melody: {args.melody}  ({len(program)} bytes)")

    if args.bytes:
        print("\nBytecode:")
        print(program.hex(" "))

    if args.disassemble:
        print("\nDisassembly:")
        for line in disassemble(program):
            print(f"  {line}")

    if args.trace:
        print("\nExecuting:")

    machine = Machine(program, trace=args.trace)

    try:
        samples = machine.run()
    except RuntimeError as error:
        print(f"\nMachine error: {error}")
        return 1

    wav_name = f"{args.melody}.wav"

    if args.quiet:
        if args.save:
            save_wav(samples, wav_name)
            print(f"\nSaved: {wav_name}")
        else:
            print(f"\n{len(samples)} samples (not playing - quiet mode)")
        return 0

    print("\nPlaying...")
    play(samples, keep_as=wav_name if args.save else None)

    if args.save:
        print(f"Saved: {wav_name}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
