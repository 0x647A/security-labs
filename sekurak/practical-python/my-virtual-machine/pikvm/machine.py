"""
Virtual machine - reads bytecode and executes it step by step.

All the work happens in a loop: fetch the instruction at the pointer,
advance the pointer, execute it. A jump is just writing a different
value into the pointer.
"""

from pikvm import assembler as asm
from pikvm.sound import make_square_wave


class Machine:
    """
    State:
      memory          the program's bytecode
      pointer         address of the next instruction
      registers       named slots for numbers
      less_than       flag set by COMPARE
      note_duration   how long a single PLAY lasts
      buffer          collected sound samples
    """

    # Safety net against programs that never finish.
    MAX_STEPS = 100_000

    def __init__(self, memory, trace=False):
        self.memory = memory
        self.trace = trace

        self.pointer = 0
        self.registers = {"a": 0, "b": 0}
        self.less_than = False
        self.note_duration = 0.15
        self.buffer = []

    # ------------------------------------------------------
    # Reading from memory
    # ------------------------------------------------------

    def _take_byte(self):
        byte = self.memory[self.pointer]
        self.pointer += 1
        return byte

    def _take_number(self):
        """Reads two bytes and combines them into one number."""
        high = self._take_byte()
        low = self._take_byte()
        return asm.from_two_bytes(high, low)

    # ------------------------------------------------------
    # Execution
    # ------------------------------------------------------

    def run(self):
        """Executes the program. Returns the collected sound samples."""
        steps = 0

        while True:
            if steps >= self.MAX_STEPS:
                raise RuntimeError(
                    f"Program didn't finish after {self.MAX_STEPS} steps "
                    "- probably stuck in an infinite loop."
                )
            steps += 1

            if self.pointer >= len(self.memory):
                raise RuntimeError(
                    f"Pointer ran past the end of memory (address {self.pointer}). "
                    "Missing a HALT instruction?"
                )

            instruction_address = self.pointer
            opcode = self._take_byte()

            if not self._execute(opcode, instruction_address):
                break

        return self.buffer

    def _execute(self, opcode, instruction_address):
        """Executes one instruction. Returns False when the program is done."""

        if opcode == asm.JUMP:
            self.pointer = self._take_number()

        elif opcode == asm.LOAD:
            self.registers["a"] = self._take_number()

        elif opcode == asm.ADD:
            self.registers["a"] += self._take_number()

        elif opcode == asm.PLAY:
            self._show(instruction_address, f"PLAY  {self.registers['a']} Hz")
            self.buffer.extend(
                make_square_wave(self.registers["a"], self.note_duration)
            )
            return True

        elif opcode == asm.COMPARE:
            self.less_than = self.registers["a"] < self._take_number()

        elif opcode == asm.JUMP_IF:
            target = self._take_number()
            if self.less_than:
                self.pointer = target

        elif opcode == asm.DURATION:
            self.note_duration = self._take_number() / 100

        elif opcode == asm.HALT:
            self._show(instruction_address, "HALT")
            return False

        else:
            raise RuntimeError(
                f"Unknown instruction {opcode} at address {instruction_address}"
            )

        self._show(instruction_address, asm.INSTRUCTIONS[opcode][0])
        return True

    # ------------------------------------------------------
    # Trace
    # ------------------------------------------------------

    def _show(self, address, description):
        if not self.trace:
            return
        print(
            f"  {address:04d}  {description:<16}"
            f"a={self.registers['a']:<6} "
            f"less_than={self.less_than}"
        )
