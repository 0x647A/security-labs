"""
Rising entrance - a loop that generates sounds that aren't in the code.

17 notes from five lines: the machine raises the pitch on its own,
until it crosses a threshold.
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
    play,
)

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
