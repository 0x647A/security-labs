"""
Sound effects straight out of 8-bit games.
"""

from pikvm.assembler import (
    add,
    assemble,
    compare,
    duration,
    halt,
    jump_if,
    label,
    load,
    note,
    play,
)
from pikvm.notes import B2, C2, E3, G2, REST

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
