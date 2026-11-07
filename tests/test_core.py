import pytest
from oces.core import Node, execute

def test_dependency_execution():
    calls = []
    def first(value):
        calls.append("first")
        return value
    def second(value):
        calls.append("second")
        return value
    result = execute([
        Node("b", "second", {"value": 2}, ("a",)),
        Node("a", "first", {"value": 1}),
    ], {"first": first, "second": second})
    assert calls == ["first", "second"]
    assert result == {"a": 1, "b": 2}

def test_cycle_rejected():
    with pytest.raises(ValueError, match="Cyclic"):
        execute([Node("a", "noop", depends_on=("b",)), Node("b", "noop", depends_on=("a",))], {"noop": lambda: None})

def test_unknown_skill_rejected():
    with pytest.raises(ValueError, match="Unknown skill"):
        execute([Node("a", "missing")], {})

def test_duplicate_id_rejected():
    with pytest.raises(ValueError, match="Duplicate"):
        execute([Node("a", "noop"), Node("a", "noop")], {"noop": lambda: None})

def test_missing_dependency_rejected():
    with pytest.raises(ValueError, match="Missing dependency"):
        execute([Node("a", "noop", depends_on=("x",))], {"noop": lambda: None})
