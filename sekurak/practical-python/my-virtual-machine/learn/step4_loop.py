"""
STEP 4 - A real loop. The machine counts to 5 on its own.

Run:  python3 step4_loop.py
"""

registers = {
    "a": 0,
    "b": 0,
}

# NEW SLOT - for the comparison result.
# It holds True or False.
less_than = False


# ============================================================
# COMMANDS
# ============================================================

#   3 = jump                  (+ where)
#   4 = load into a           (+ number)
#   5 = add to a               (+ number)
#   6 = show a
#   7 = COMPARE a to a number  (+ number)   -> stores the result in "less_than"
#   8 = JUMP IF less_than      (+ where)
#   9 = halt

memory = [
    4, 1,      # 0,1:  load 1 into a

    # --- the loop starts here (slot 2) ---
    6,         # 2:    show a
    5, 1,      # 3,4:  add 1 to a
    7, 6,      # 5,6:  compare: is a < 6 ?
    8, 2,      # 7,8:  if so -> jump to slot 2
    # --- end of loop ---

    9,         # 9:    halt
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
        print("a =", registers["a"])

    elif command == 7:
        # COMPARE - check and REMEMBER the result.
        # It doesn't do anything by itself, just stores the answer for later.
        number = memory[position]
        position = position + 1

        less_than = registers["a"] < number

    elif command == 8:
        # JUMP IF - only jumps when "less_than" is true.
        target = memory[position]
        position = position + 1

        if less_than:
            position = target
        # if false - do nothing, the finger keeps moving forward

    elif command == 9:
        print("(halt)")
        break

    else:
        print("Unknown command:", command)
        break
