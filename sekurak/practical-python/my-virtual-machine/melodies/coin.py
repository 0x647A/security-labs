"""
Sound effects straight out of 8-bit games.
"""

from pikvm.assembler import (
    duration, add, label, play, halt, note, compare, jump_if,
    load, assemble,
)
from pikvm.notes import REST, C2, E3, B2, G2

program = assemble(
    # Picking up a coin - two quick rising sounds.
    duration(8),
    note(B2),
    duration(25),
    note(E3),

    duration(30),
    note(REST),

    # Jump - a fast rising sweep.
    duration(3),
    load(300),
    label("jump"),
    play(),
    add(120),
    compare(1400),
    jump_if("jump"),

    duration(30),
    note(REST),

    # Losing a life - descending.
    duration(12),
    note(G2),
    note(C2),
    duration(35),
    note(200),

    halt(),
)
