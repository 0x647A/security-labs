"""
Speaker - turns numbers into sound.

We generate a square wave: one that jumps between two values with
nothing in between. That's where the characteristic "8-bit" sound
of old consoles comes from.
"""

import os
import struct
import subprocess
import sys
import wave

# How many samples (numbers) describe one second of sound. 44100 is the CD standard.
SAMPLE_RATE = 44100

# How far the speaker cone moves. The 16-bit range is -32768..32767; we use less.
VOLUME = 6000


def make_square_wave(frequency_hz, duration_seconds):
    """
    Returns a list of samples for a sound of the given pitch and length.

    frequency_hz       pitch of the sound (0 = silence)
    duration_seconds   how long it should last
    """
    sample_count = int(SAMPLE_RATE * duration_seconds)

    if frequency_hz <= 0:
        return [0] * sample_count

    samples_per_cycle = SAMPLE_RATE / frequency_hz

    samples = []
    for sample_number in range(sample_count):
        position_in_cycle = sample_number % samples_per_cycle

        # First half of the cycle goes up, second half goes down. Nothing in between.
        if position_in_cycle < samples_per_cycle / 2:
            samples.append(VOLUME)
        else:
            samples.append(-VOLUME)

    return samples


def save_wav(samples, file_name):
    """Saves samples as a .wav file (mono, 16-bit)."""
    with wave.open(file_name, "wb") as file:
        file.setnchannels(1)
        file.setsampwidth(2)
        file.setframerate(SAMPLE_RATE)
        file.writeframes(struct.pack("<" + "h" * len(samples), *samples))


def _player_command(file_name):
    """Picks a player for the current OS."""
    if sys.platform == "darwin":
        return ["afplay", file_name]
    if sys.platform.startswith("linux"):
        return ["aplay", "-q", file_name]
    if sys.platform == "win32":
        return [
            "powershell", "-c",
            f"(New-Object Media.SoundPlayer '{file_name}').PlaySync()",
        ]
    return None


def play(samples, keep_as=None):
    """
    Plays the samples.

    keep_as   if you pass a file name, the .wav is kept on disk
              instead of being deleted after playback
    """
    if not samples:
        return

    file_name = keep_as or "_temp_sound.wav"
    save_wav(samples, file_name)

    command = _player_command(file_name)
    if command is None:
        print(f"No known player for this system. File: {file_name}")
        return

    try:
        subprocess.run(command, check=False)
    except FileNotFoundError:
        print(f"Missing player '{command[0]}'. File saved: {file_name}")
        return

    if keep_as is None:
        os.remove(file_name)
