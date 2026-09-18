# pikVM

A virtual machine that plays music.

An imaginary 8-bit computer written in Python: it has its own instruction set,
its own assembler, and a speaker that generates a square wave - the sound of
old game consoles. A bytecode program drives the synthesizer.

No external dependencies - standard library only.

## Quick start

```bash
python3 play.py               # list melodies
python3 play.py cat           # play one
```

## What it looks like

A program is written as Python function calls:

```python
program = assemble(
    duration(6),
    load(200),

    label("rising"),
    play(),
    add(60),
    compare(1200),
    jump_if("rising"),

    halt(),
)
```

The assembler turns this into 17 bytes:

```
0a 00 06 04 00 c8 06 05 00 3c 07 04 b0 08 00 06 09
```

And the machine executes them - producing a rising sweep of sound. Seventeen
notes, none of which are written in the code: a loop generates them.

## Execution trace

```bash
python3 play.py entrance --trace
```

```
  0000  DURATION        a=0      less_than=False
  0003  LOAD            a=200    less_than=False
  0006  PLAY  200 Hz    a=200    less_than=False
  0007  ADD             a=260    less_than=False
  0010  COMPARE         a=260    less_than=True
  0013  JUMP_IF         a=260    less_than=True
  0006  PLAY  260 Hz    a=260    less_than=True
```

Notice the jump: from address `0013`, the pointer goes back to `0006`. That's
the whole secret of a loop - writing a different value into the program
counter.

## Disassembler

Bytecode back to text:

```bash
python3 play.py entrance --disassemble
```

```
  0000:  DURATION 6
  0003:  LOAD 200
  0006:  PLAY
  0007:  ADD 60
  0010:  COMPARE 1200
  0013:  JUMP_IF 6
  0016:  HALT
```

## Architecture

**Memory** - a `bytearray`, shared by code and data.

**Registers** - `a` (pitch, the result of computations) and `b`. The
`less_than` flag is set by `COMPARE`.

**Pointer** - the address of the next instruction.

**Multi-byte numbers** - a byte only holds 0-255, but frequencies run into
the thousands of Hz. Larger values take up two bytes:
`[number // 256, number % 256]`.

### Instructions

| Opcode | Mnemonic | Argument | Effect |
|--------|----------|----------|-----------|
| 3 | `JUMP` | address (2B) | pointer = address |
| 4 | `LOAD` | number (2B) | a = number |
| 5 | `ADD` | number (2B) | a += number |
| 6 | `PLAY` | - | play a sound at pitch a |
| 7 | `COMPARE` | number (2B) | less_than = (a < number) |
| 8 | `JUMP_IF` | address (2B) | jump, if less_than |
| 9 | `HALT` | - | stop |
| 10 | `DURATION` | hundredths of a sec (2B) | length of the following sounds |

## Assembler

Labels are resolved in **two passes**. Reason: a jump can point at a label
further ahead in the code, whose address isn't known yet.

The first pass emits bytes and records label positions, leaving gaps where
jump addresses go. The second pass goes back to those gaps and fills them
with the real values.

## Sound

A square wave jumps between two values, with nothing in between:

```
+6000  ████    ████    ████
     0 ----████----████----
-6000      ████    ████
```

Hence the sharp, synthetic sound. Old computers worked this way because all
they could do was switch the current to the speaker on and off.

Samples are collected into a buffer and played once at the end - playing
each note separately would leave audible gaps.

## Structure

```
pikvm/
    sound.py        wave generation and playback
    notes.py        note names
    assembler.py    bytecode + disassembler
    machine.py      execution
melodies/           example programs
learn/              the stages the project went through while being built
play.py             runner
```

The `learn/` directory holds nine steps showing how the project came
together - from a machine that just prints "hi" to the full virtual machine.
Each file runs on its own.

## Options

```
--trace         step-by-step execution
--disassemble   bytecode as text
--bytes         raw bytes
--save          save a .wav
--quiet         don't play
```

## Writing your own melody

A new file in `melodies/`:

```python
from pikvm.assembler import duration, halt, note, assemble
from pikvm.notes import C, E, G

program = assemble(
    duration(20),
    note(C), note(E), note(G),
    halt(),
)
```

```bash
python3 play.py file_name
```

## Requirements

Python 3.8+. Playback: `afplay` (macOS), `aplay` (Linux), PowerShell (Windows).
Without a player, `--save` still works.
