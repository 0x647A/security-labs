"""
"Wlazł kotek na płotek" (a Polish children's song, "The Cat Climbed the Fence")
- melody written out note by note.
"""

from pikvm.assembler import assemble, duration, halt, note
from pikvm.notes import REST, C, D, E, F, G

program = assemble(
    duration(20),

    note(G), note(E), note(E),
    note(F), note(D), note(D),
    note(C), note(E), note(G),
    note(G), note(E), note(E),

    note(REST),

    halt(),
)
