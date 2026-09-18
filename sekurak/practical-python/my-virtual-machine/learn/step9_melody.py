"""
STEP 9 - Melody.

We add:
  - note names (C, D, E... instead of numbers)
  - note duration (a new command)
  - a rest

Run:  python3 step9_melody.py
"""

import os
import struct
import subprocess
import wave

# ============================================================
# SPEAKER
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
# NOTES - names instead of numbers
# ============================================================

REST = 0

C  = 262
D  = 294
E  = 330
F  = 349
G  = 392
A  = 440
B  = 494
C2 = 523      # one octave up
D2 = 587
E2 = 659


# ============================================================
# NUMBER ACROSS TWO BYTES
# ============================================================

def to_two_bytes(number):
    return [number // 256, number % 256]


def from_two_bytes(high, low):
    return high * 256 + low


# ============================================================
# ASSEMBLER
# ============================================================

#   3 = jump                (+ address)
#   4 = load into a         (+ number)
#   5 = add to a            (+ number)
#   6 = play
#   7 = compare a           (+ number)
#   8 = jump if
#   9 = halt
#  10 = SET DURATION        (+ number, in hundredths of a second)   <- NEW

def load(number):
    return [4] + to_two_bytes(number)

def add(number):
    return [5] + to_two_bytes(number)

def play_note():
    return [6]

def compare(number):
    return [7] + to_two_bytes(number)

def halt():
    return [9]

def duration(hundredths):
    """How long each following sound should last. 15 = 0.15 seconds."""
    return [10] + to_two_bytes(hundredths)


def note(pitch):
    """Shortcut: set the pitch AND play it right away."""
    return load(pitch) + play_note()


class Label:
    def __init__(self, name):
        self.name = name

def label(name):
    return Label(name)


class Jump:
    def __init__(self, name, opcode):
        self.name = name
        self.opcode = opcode

def jump(name):
    return Jump(name, 3)

def jump_if(name):
    return Jump(name, 8)


def assemble(*commands):
    result = []
    labels = {}
    to_fix = []

    for command in commands:

        if isinstance(command, Label):
            labels[command.name] = len(result)
            continue

        if isinstance(command, Jump):
            result.append(command.opcode)
            to_fix.append((command, len(result)))
            result.extend([0, 0])
            continue

        result.extend(command)

    for jmp, where in to_fix:
        high, low = to_two_bytes(labels[jmp.name])
        result[where] = high
        result[where + 1] = low

    return bytearray(result)


# ============================================================
# PROGRAM - a melody!
# ============================================================

memory = assemble(
    duration(20),          # each sound lasts 0.20 seconds

    # --- "Wlazł kotek na płotek" (a Polish children's song) ---
    note(G), note(E), note(E),
    note(F), note(D), note(D),
    note(C), note(E), note(G),
    note(G), note(E), note(E),

    note(REST),            # a short pause

    # --- and now a LOOP: a rising sweep of sound ---
    duration(6),           # short, quick sounds
    load(200),

    label("rising"),
    play_note(),
    add(60),
    compare(1200),
    jump_if("rising"),

    halt(),
)

print("memory:", memory.hex(" "))
print("bytes:", len(memory))


# ============================================================
# MACHINE
# ============================================================

buffer = []

registers = {
    "a": 0,
    "b": 0,
}

less_than = False
position = 0

# NEW: the machine remembers how long a sound should last.
note_duration = 0.15


def take_number():
    global position
    high = memory[position]
    low = memory[position + 1]
    position = position + 2
    return from_two_bytes(high, low)


while True:

    command = memory[position]
    position = position + 1

    if command == 3:
        position = take_number()

    elif command == 4:
        registers["a"] = take_number()

    elif command == 5:
        registers["a"] = registers["a"] + take_number()

    elif command == 6:
        buffer.extend(make_square_wave(registers["a"], note_duration))

    elif command == 7:
        less_than = registers["a"] < take_number()

    elif command == 8:
        target = take_number()
        if less_than:
            position = target

    elif command == 9:
        print("(halt)")
        break

    elif command == 10:
        # SET DURATION - we get hundredths of a second, convert to seconds
        note_duration = take_number() / 100

    else:
        print("Unknown command:", command)
        break


print("playing...")
play(buffer)
