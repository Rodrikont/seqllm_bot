from dataclasses import dataclass, field

@dataclass
class UscaseSolverResponse:
    status: str
    roots: list = field(default_factory=list)
    aproxRoots: list = field(default_factory=list)