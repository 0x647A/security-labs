"""
STEP 5 - The machine plays sound.

This is step 4, but "show a" becomes "play a".

Run:  python3 step5_speaker.py

Note: this uses `afplay`, which only exists on macOS. On Linux or
Windows, see pikvm/sound.py for a cross-platform player.
"""

import struct
import wave
import subprocess
import os


# ============================================================
# SPEAKER - same as in step 0
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
# BUFFER - where we collect sounds
# ============================================================

# IMPORTANT: we don't play each note separately, because there
# would be gaps between notes (the player would have to start up
# every single time).
#
# Instead: we collect everything into one list,
# and play it ONCE at the end.

buffer = []


# ============================================================
# MACHINE
# ============================================================

registers = {
    "a": 0,
    "b": 0,
}

less_than = False


#   3 = jump                   (+ where)
#   4 = load into a            (+ number)
#   5 = add to a                (+ number)
#   6 = PLAY a                              <- CHANGED! used to be "show"
#   7 = compare a to a number   (+ number)
#   8 = jump if less_than       (+ where)
#   9 = halt

memory = [
    4, 262,     # 0,1:  load 262 into a   (this is the note "C")

    # --- loop ---
    6,          # 2:    play a
    5, 40,      # 3,4:  add 40 to a   (raise the pitch)
    7, 500,     # 5,6:  is a < 500 ?
    8, 2,       # 7,8:  if so -> go back to slot 2
    # --- end of loop ---

    9,          # 9:    halt
]

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
        # PLAY - append a sound to the buffer.
        # Slot "a" is now the PITCH OF THE SOUND.
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


# ============================================================
# AT THE END - play everything at once
# ============================================================

print("playing...")
play(buffer)
