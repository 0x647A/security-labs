"""
Assembler - turns readable commands into bytecode.

Each function returns a list of bytes. `assemble()` glues them into
one memory blob and resolves labels.
"""


# ============================================================
# INSTRUCTION SET
# ============================================================

JUMP        = 3    # + address (2 bytes)
LOAD        = 4    # + number (2 bytes)
ADD         = 5    # + number (2 bytes)
PLAY        = 6
COMPARE     = 7    # + number (2 bytes)
JUMP_IF     = 8    # + address (2 bytes)
HALT        = 9
DURATION    = 10   # + hundredths of a second (2 bytes)

# Names and argument lengths - used by the disassembler.
INSTRUCTIONS = {
    JUMP:     ("JUMP",     2),
    LOAD:     ("LOAD",     2),
    ADD:      ("ADD",      2),
    PLAY:     ("PLAY",     0),
    COMPARE:  ("COMPARE",  2),
    JUMP_IF:  ("JUMP_IF",  2),
    HALT:     ("HALT",     0),
    DURATION: ("DURATION", 2),
}


# ============================================================
# MULTI-BYTE NUMBERS
# ============================================================

# A single byte only holds 0-255, so bigger numbers get split
# into two bytes: how many full 256s + what's left over.

MAX_NUMBER = 65535


def to_two_bytes(number):
    if not 0 <= number <= MAX_NUMBER:
        raise ValueError(f"Number {number} outside range 0..{MAX_NUMBER}")
    return [number // 256, number % 256]


def from_two_bytes(high, low):
    return high * 256 + low


# ============================================================
# COMMANDS
# ============================================================

def load(number):
    """Load a number into register A."""
    return [LOAD] + to_two_bytes(number)


def add(number):
    """Add a number to register A."""
    return [ADD] + to_two_bytes(number)


def play():
    """Play the pitch currently held in register A."""
    return [PLAY]


def compare(number):
    """Check whether A < number. The result goes into the flag."""
    return [COMPARE] + to_two_bytes(number)


def duration(hundredths):
    """Set the length of the notes that follow. 20 = 0.20 seconds."""
    return [DURATION] + to_two_bytes(hundredths)


def halt():
    """Stop the machine."""
    return [HALT]


def note(pitch):
    """Shortcut: set the pitch and play it right away."""
    return load(pitch) + play()


# ============================================================
# LABELS AND JUMPS
# ============================================================

class Label:
    """A marker for a place in the code. Takes up no bytes."""

    def __init__(self, name):
        self.name = name


class Jump:
    """A jump to a label. The address is filled in on the second pass."""

    def __init__(self, name, opcode):
        self.name = name
        self.opcode = opcode


def label(name):
    return Label(name)


def jump(name):
    """Always jump."""
    return Jump(name, JUMP)


def jump_if(name):
    """Jump if the last comparison was true."""
    return Jump(name, JUMP_IF)


# ============================================================
# ASSEMBLING
# ============================================================

def assemble(*commands):
    """
    Glues commands into bytecode and turns labels into addresses.

    Two passes, because a jump can point at a label that appears
    later in the code - at the point the jump is emitted, that
    address isn't known yet. So we leave a gap and come back to it
    at the end.
    """
    result = []
    labels = {}
    to_fix = []

    # Pass 1: emit bytes, collect label addresses.
    for command in commands:

        if isinstance(command, Label):
            if command.name in labels:
                raise ValueError(f"Label '{command.name}' already exists")
            labels[command.name] = len(result)
            continue

        if isinstance(command, Jump):
            result.append(command.opcode)
            to_fix.append((command, len(result)))
            result.extend([0, 0])
            continue

        result.extend(command)

    # Pass 2: fill the gaps with real addresses.
    for jmp, where in to_fix:
        if jmp.name not in labels:
            raise ValueError(f"No such label '{jmp.name}'")
        high, low = to_two_bytes(labels[jmp.name])
        result[where] = high
        result[where + 1] = low

    return bytearray(result)


# ============================================================
# DISASSEMBLER
# ============================================================

def disassemble(memory):
    """
    The reverse of `assemble` - turns bytecode back into readable text.

    Returns a list of strings, one per instruction.
    """
    lines = []
    address = 0

    while address < len(memory):
        opcode = memory[address]

        if opcode not in INSTRUCTIONS:
            lines.append(f"{address:04d}:  ??? ({opcode})")
            address += 1
            continue

        name, arg_count = INSTRUCTIONS[opcode]

        if arg_count == 0:
            lines.append(f"{address:04d}:  {name}")
            address += 1
        else:
            if address + 2 >= len(memory):
                lines.append(f"{address:04d}:  {name} (truncated argument)")
                break
            value = from_two_bytes(memory[address + 1], memory[address + 2])
            lines.append(f"{address:04d}:  {name} {value}")
            address += 3

    return lines
