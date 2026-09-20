# How this project came together

Nine steps from the simplest machine to one that plays music.
Each file runs on its own - just `python3 name.py`.

| File | What it adds |
|------|-------------|
| `test_sound.py` | a square wave - checking whether we can make any sound at all |
| `step1_machine.py` | memory, pointer, the "fetch-execute" loop |
| `step2_jump.py` | jump - writing a different value into the pointer |
| `step3_registers.py` | registers, i.e. slots for numbers |
| `step4_loop.py` | comparison and conditional jump -> a real loop |
| `step5_speaker.py` | hooking up sound: register `a` becomes the pitch |
| `step6_assembler.py` | functions that produce bytecode instead of raw numbers |
| `step7_labels.py` | jumps by name, two-pass address resolution |
| `step8_bytes.py` | `bytearray` and numbers across two bytes |
| `step9_melody.py` | note names, note duration, a rest |

Steps 1-4 make no sound - they show the execution mechanism on its own.

Step 7 is the most interesting: resolving labels needs two passes, because a
forward jump points at an address that isn't known yet at the point it's
encountered.
