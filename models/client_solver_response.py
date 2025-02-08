from dataclasses import dataclass, field
from typing import Optional

@dataclass
class ClientSolverResponse:
    status: str
    roots: list = field(default_factory=list)
    aproxRoots: list = field(default_factory=list)
    answer: Optional[str] = None
    error: Optional[str] = None