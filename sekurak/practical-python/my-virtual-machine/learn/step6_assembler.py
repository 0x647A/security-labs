"""
STEP 6 - Assembler. Instead of writing numbers, we write functions.

Run:  python3 step6_assembler.py
"""

import struct
import wave
import subprocess
import os


# ============================================================
# SPEAKER (unchanged)
# ============================================================

SAMPLE_RATE = 44100
VOLUME = 6000


def make_square_wave(frequency_hz, duration_seconds):
    sample_count = int(SAMPLE_RATE * duration_seconds)

    if frequency_hz == 0:
        return [0] * sample_count

    samples_per_cycle = SAMPLE_RATE / frequency_hz

    samples = []
    for sample_number in range(sample_count):
        position_in_cycle = sample_number % samples_per_cycle
        if position_in_cycle < samples_per_cycle / 2:
            samples.append(VOLUME)
        else:
            samples.append(-VOLUME)

    return samples


def play(samples):
    file_name = "_temp_sound.wav"

    with wave.open(file_name, "wb") as file:
        file.setnchannels(1)
        file.setsampwidth(2)
        file.setframerate(SAMPLE_RATE)
        data = struct.pack("<" + "h" * len(samples), *samples)
        file.writeframes(data)

    subprocess.run(["afplay", file_name])
    os.remove(file_name)


# ============================================================
# ASSEMBLER - functions that produce numbers
# ============================================================

# Each function returns a LIST of numbers - one command.
# That's it. No magic.

def jump(target):
    return [3, target]

def load(number):
    return [4, number]

def add(number):
    return [5, number]

def play_note():
    return [6]

def compare(number):
    return [7, number]

def jump_if(target):
    return [8, target]

def halt():
    return [9]


def assemble(*commands):
    """
    Glues all commands into one list of numbers.

    The star (*) means: "accept any number of arguments
    and put them into a list called commands".
    """
    result = []
    for command in commands:
        result.extend(command)
    return result


# ============================================================
# PROGRAM - now readable!
# ============================================================

memory = assemble(
    load(262),        # slot 0, 1

    play_note(),       # slot 2      <- we come back here
    add(40),           # slot 3, 4
    compare(500),      # slot 5, 6
    jump_if(2),        # slot 7, 8

    halt(),            # slot 9
)

print("bytecode:", memory)


# ============================================================
# MACHINE (unchanged)
# ============================================================

buffer = []

registers = {
    "a": 0,
    "b": 0,
}

less_than = False
position = 0


while True:

    command = memory[position]
    position = position + 1

    if command == 3:
        target = memory[position]
        position = position + 1
        position = target

    elif command == 4:
        number = memory[position]
        position = position + 1
        registers["a"] = number

    elif command == 5:
        number = memory[position]
        position = position + 1
        registers["a"] = registers["a"] + number

    elif command == 6:
        print("playing:", registers["a"], "Hz")
        buffer.extend(make_square_wave(registers["a"], 0.15))

    elif command == 7:
        number = memory[position]
        position = position + 1
        less_than = registers["a"] < number

    elif command == 8:
        target = memory[position]
        position = position + 1
        if less_than:
            position = target

    elif command == 9:
        print("(halt)")
        break

    else:
        print("Unknown command:", command)
        break


print("playing...")
play(buffer)
