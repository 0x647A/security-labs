"""
STEP 8 - Real memory: bytearray.

PROBLEM: a byte only holds 0-255.
         And 262 Hz doesn't fit!

SOLUTION: numbers bigger than 255 get stored across TWO bytes.

Run:  python3 step8_bytes.py
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
# A NUMBER ACROSS TWO BYTES
# ============================================================

def to_two_bytes(number):
    """
    Turns a number (0-65535) into two bytes.

    Example: 262
      262 divided by 256 = 1, remainder 6
      so: [1, 6]

    The first byte says "how many full 256s".
    The second byte says "how much is left over".
    """
    high = number // 256      # // is division without a remainder
    low = number % 256        # % is just the remainder
    return [high, low]


def from_two_bytes(high, low):
    """The reverse: combines two bytes back into a number."""
    return high * 256 + low


# ============================================================
# ASSEMBLER
# ============================================================

# NOTE: commands with big numbers now take up THREE slots:
#       opcode + high byte + low byte

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

    # ---- PASS 1 ----
    for command in commands:

        if isinstance(command, Label):
            labels[command.name] = len(result)
            continue

        if isinstance(command, Jump):
            result.append(command.opcode)
            to_fix.append((command, len(result)))
            result.extend([0, 0])      # TWO zeros - the address needs two bytes too
            continue

        result.extend(command)

    # ---- PASS 2 ----
    for jmp, where_the_gap_is in to_fix:
        address = labels[jmp.name]
        high, low = to_two_bytes(address)
        result[where_the_gap_is] = high
        result[where_the_gap_is + 1] = low

    # AND HERE'S WHAT'S NEW - turn the list into REAL MEMORY.
    return bytearray(result)


# ============================================================
# PROGRAM
# ============================================================

memory = assemble(
    load(262),

    label("start"),
    play_note(),
    add(40),
    compare(500),
    jump_if("start"),

    halt(),
)

# Show the memory the way byte-inspection tools usually do:
# each byte as two hex digits.
print("memory:", memory.hex(" "))
print("as list:", list(memory))


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


def take_number():
    """
    Reads TWO bytes from memory and combines them into a number.
    Also moves the pointer forward by two slots.
    """
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
        print("playing:", registers["a"], "Hz")
        buffer.extend(make_square_wave(registers["a"], 0.15))

    elif command == 7:
        less_than = registers["a"] < take_number()

    elif command == 8:
        target = take_number()
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
