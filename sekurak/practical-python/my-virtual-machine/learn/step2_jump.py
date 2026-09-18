"""
STEP 2 - Jump. The machine can go back to an earlier command.

Run:  python3 step2_jump.py
"""

# ============================================================
# NEW COMMAND: 3 = jump
# ============================================================

#   1 = say "hi"
#   2 = say "bye"
#   3 = JUMP  (followed by a SECOND number: where to jump to)
#   9 = halt

# Note: command 3 takes up TWO slots in memory.
# The first says "jump", the second says "where".

memory = [
    1,        # slot 0: say "hi"
    2,        # slot 1: say "bye"
    3, 0,     # slot 2 and 3: jump to slot 0
]

position = 0

# Counter so the program doesn't spin forever.
step_count = 0


while True:

    # Safety net - stop after 10 commands.
    step_count = step_count + 1
    if step_count > 10:
        print("(stop - too many steps)")
        break

    # FETCH
    command = memory[position]

    # ADVANCE
    position = position + 1

    # DO
    if command == 1:
        print("hi")

    elif command == 2:
        print("bye")

    elif command == 3:
        # Take the NEXT number - that's the jump target.
        target = memory[position]
        position = position + 1

        # AND THIS IS THE WHOLE JUMP:
        # instead of moving the finger by one, we WRITE it a new spot.
        position = target

    elif command == 9:
        print("(halt)")
        break

    else:
        print("Unknown command:", command)
        break
