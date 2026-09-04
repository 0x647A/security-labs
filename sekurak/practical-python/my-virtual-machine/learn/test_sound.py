"""
STEP 0 - Checking whether we can make any sound at all.

This is NOT the virtual machine yet. It's just a test that we can
make a "pixel art" sound. We'll build the machine on top of this.

Run:  python3 test_sound.py
"""

import struct     # for turning numbers into bytes
import wave       # for writing a .wav file
import subprocess # for launching the system player
import os         # for removing the temp file


# ============================================================
# SETTINGS
# ============================================================

# How many numbers (samples) describe ONE SECOND of sound.
# 44100 is the CD standard. More means a more accurate sound.
SAMPLE_RATE = 44100

# How hard the speaker cone moves.
# Samples are stored as 16-bit numbers, so they fit in the range
# -32768 to +32767. We use less, so it isn't too loud.
VOLUME = 6000


# ============================================================
# GENERATING A SQUARE WAVE
# ============================================================

def make_square_wave(frequency_hz, duration_seconds):
    """
    Creates a list of numbers describing a sound at the given pitch.

    frequency_hz - the pitch of the sound. How many times per second
                   the wave completes a full cycle (up and down).
                   440 Hz is the note "A" - the one guitars are tuned to.
                   More Hz = a higher sound.

    duration_seconds - how long it should last.
    """

    # How many samples we need to produce in total.
    # E.g. 0.5 seconds * 44100 samples per second = 22050 samples.
    sample_count = int(SAMPLE_RATE * duration_seconds)

    # Silence is just zeros - the cone doesn't move.
    if frequency_hz == 0:
        return [0] * sample_count

    # How many samples make up ONE full wave cycle (once up, once down).
    # At 440 Hz: 44100 / 440 = about 100 samples per cycle.
    samples_per_cycle = SAMPLE_RATE / frequency_hz

    samples = []
    for sample_number in range(sample_count):

        # Where in the cycle are we?
        # The remainder from division (%) makes the number "wrap around"
        # back to zero after every full cycle.
        # E.g. with a cycle of 100: 0,1,2...99,0,1,2...99,0,...
        position_in_cycle = sample_number % samples_per_cycle

        # AND HERE'S ALL THE "PIXEL ART" MAGIC:
        # first half of the cycle -> cone pushed all the way forward
        # second half of the cycle -> cone pulled all the way back
        # No values in between. Just two states.
        if position_in_cycle < samples_per_cycle / 2:
            samples.append(VOLUME)
        else:
            samples.append(-VOLUME)

    return samples


# ============================================================
# SAVING TO A FILE AND PLAYING IT
# ============================================================

def play(samples):
    """
    Saves a list of numbers as a .wav file and plays it.
    """

    file_name = "_temp_sound.wav"

    # Open the .wav file for writing ("wb" = write binary)
    with wave.open(file_name, "wb") as file:
        file.setnchannels(1)                # 1 = mono (one speaker)
        file.setsampwidth(2)                # 2 bytes per sample = 16 bits
        file.setframerate(SAMPLE_RATE)      # samples per second

        # Turn the list of numbers into raw bytes.
        # "<" means little-endian, "h" means a signed 16-bit number
        # (i.e. one that can be negative).
        # It's the same struct module mentioned in class!
        data = struct.pack("<" + "h" * len(samples), *samples)
        file.writeframes(data)

    # Play it through the macOS system player.
    subprocess.run(["afplay", file_name])

    # Clean up after ourselves.
    os.remove(file_name)


# ============================================================
# TEST
# ============================================================

if __name__ == "__main__":

    print("Test 1: a single A note (440 Hz)...")
    play(make_square_wave(440, 0.5))

    print("Test 2: a rising scale...")
    # Frequencies of the notes in a C major scale
    scale = [262, 294, 330, 349, 392, 440, 494, 523]
    all_samples = []
    for frequency in scale:
        all_samples += make_square_wave(frequency, 0.15)
    play(all_samples)

    print("Test 3: a 'coin pickup' sound (like from a game)...")
    coin = (
        make_square_wave(988, 0.08) +   # short high sound
        make_square_wave(1319, 0.25)    # and an even higher, longer one
    )
    play(coin)

    print("Done!")
