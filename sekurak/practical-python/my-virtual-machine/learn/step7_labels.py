"""
STEP 7 - Labels. Jumps by name instead of by number.

Run:  python3 step7_labels.py
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
# ASSEMBLER
# ============================================================

# Regular commands - unchanged.

def load(number):
    return [4, number]

def add(number):
    return [5, number]

def play_note():
    return [6]

def compare(number):
    return [7, number]

def halt():
    return [9]


# --- NEW: label ---

class Label:
    """A marker in the code. Produces no number by itself."""
    def __init__(self, name):
        self.name = name

def label(name):
    return Label(name)


# --- NEW: jumps by name ---

class Jump:
    """A jump to a label. Doesn't know the target slot yet."""
    def __init__(self, name, opcode):
        self.name = name
        self.opcode = opcode

def jump(name):
    return Jump(name, 3)

def jump_if(name):
    return Jump(name, 8)


# --- Assembling ---

def assemble(*commands):
    """
    Glues commands into a list of numbers and turns label names into slot numbers.

    We do this in TWO PASSES:

      Pass 1 - walk through the code, note where each label is,
               and insert a temporary zero wherever a jump appears.

      Pass 2 - go back to those zeros and write in the real numbers.

    Why two? Because a jump can point at a label that's FURTHER AHEAD
    in the code - and at pass 1 we don't know it yet.
    """

    result = []
    labels = {}          # name -> slot number
    to_fix = []           # (jump object, where its argument lives)

    # ---- PASS 1 ----
    for command in commands:

        if isinstance(command, Label):
            # A label takes up no space. We just remember that
            # it sits at THIS point in the code.
            labels[command.name] = len(result)
            continue

        if isinstance(command, Jump):
            result.append(command.opcode)

            # We don't know the target yet. Insert a zero for now
            # and remember where that zero lives.
            to_fix.append((command, len(result)))
            result.append(0)
            continue

        # A regular command - just append it.
        result.extend(command)

    # ---- PASS 2 ----
    for jmp, where_the_zero_is in to_fix:
        result[where_the_zero_is] = labels[jmp.name]

    return result


# ============================================================
# PROGRAM - no more counting slots!
# ============================================================

memory = assemble(
    load(262),

    label("start"),           # <- a name instead of a number
    play_note(),
    add(40),
    compare(500),
    jump_if("start"),          # <- jump to the name

    halt(),
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
