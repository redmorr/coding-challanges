from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Node:
    val: str
    next: Node
