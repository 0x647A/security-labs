"""
STEP 1 - A machine that reads commands and executes them.

No sound yet. We just want to see the mechanism itself.

Run:  python3 step1_machine.py
"""

# ============================================================
# 1. MEMORY - where the commands live
# ============================================================

# Our commands are NUMBERS. We agree on what each one means:
#
#   1 = say "hi"
#   2 = say "bye"
#   9 = halt
#
# This is just a convention. We made it up. It could be different.

memory = [1, 2, 1, 9]


# ============================================================
# 2. POINTER - where we are right now
# ============================================================

# The machine has to remember which command it's reading.
# It's just a number: 0 = first command, 1 = second, and so on.

position = 0


# ============================================================
# 3. LOOP - read and execute, over and over
# ============================================================

while True:

    # FETCH the command at the current position
    command = memory[position]

    # ADVANCE to the next one
    position = position + 1

    # LOOK at what the command is, and DO it
    if command == 1:
        print("hi")

    elif command == 2:
        print("bye")

    elif command == 9:
        print("(halt)")
        break        # break = exit the loop

    else:
        print("Unknown command:", command)
        break
