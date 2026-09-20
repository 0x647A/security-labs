"""
STEP 3 - Registers. Slots where the machine keeps numbers.

Run:  python3 step3_registers.py
"""

# ============================================================
# REGISTERS = slots for numbers
# ============================================================

# The machine has two slots: "a" and "b".
# Both start out at zero.

registers = {
    "a": 0,
    "b": 0,
}


# ============================================================
# COMMANDS
# ============================================================

#   1 = say "hi"
#   2 = say "bye"
#   3 = jump           (+ where)
#   4 = LOAD into a    (+ which number)      a = number
#   5 = ADD to a       (+ which number)      a = a + number
#   6 = SHOW a
#   9 = halt

memory = [
    4, 10,    # load 10 into slot a
    6,        # show a
    5, 5,     # add 5 to a
    6,        # show a
    5, 5,     # add 5 to a
    6,        # show a
    9,        # halt
]

position = 0


while True:

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
        target = memory[position]
        position = position + 1
        position = target

    elif command == 4:
        # LOAD a number into slot "a"
        number = memory[position]
        position = position + 1

        registers["a"] = number

    elif command == 5:
        # ADD a number to whatever is already in "a"
        number = memory[position]
        position = position + 1

        registers["a"] = registers["a"] + number

    elif command == 6:
        # SHOW what's in "a"
        print("a =", registers["a"])

    elif command == 9:
        print("(halt)")
        break

    else:
        print("Unknown command:", command)
        break
