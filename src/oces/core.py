"""Small, deterministic skill graph engine. No arbitrary code execution."""
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Callable

@dataclass(frozen=True)
class Node:
    id: str
    skill: str
    inputs: dict[str, Any] = field(default_factory=dict)
    depends_on: tuple[str, ...] = ()

def execute(nodes: list[Node], registry: dict[str, Callable[..., Any]]) -> dict[str, Any]:
    ids = [n.id for n in nodes]
    if len(ids) != len(set(ids)):
        raise ValueError("Duplicate node IDs")
    by_id = {n.id: n for n in nodes}
    for n in nodes:
        if n.skill not in registry:
            raise ValueError(f"Unknown skill: {n.skill}")
        for dependency in n.depends_on:
            if dependency not in by_id:
                raise ValueError(f"Missing dependency: {dependency}")
    results: dict[str, Any] = {}
    visiting: set[str] = set()
    def visit(node_id: str) -> None:
        if node_id in results:
            return
        if node_id in visiting:
            raise ValueError("Cyclic dependency")
        visiting.add(node_id)
        node = by_id[node_id]
        for dependency in node.depends_on:
            visit(dependency)
        results[node_id] = registry[node.skill](**node.inputs)
        visiting.remove(node_id)
    for node in nodes:
        visit(node.id)
    return results

def inspect_ifc(path: str) -> dict[str, Any]:
    import ifcopenshell
    file_path = Path(path)
    if not file_path.is_file():
        raise FileNotFoundError(path)
    model = ifcopenshell.open(str(file_path))
    elements = model.by_type("IfcElement")
    return {
        "schema": model.schema,
        "element_count": len(elements),
        "elements": [
            {"guid": e.GlobalId, "type": e.is_a(), "name": e.Name}
            for e in elements
        ],
    }
