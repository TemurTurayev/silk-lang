"""
Golden Tests

Tests that compare program output against expected output files.
"""

import pytest
from pathlib import Path
from silk.interpreter import Interpreter


GOLDEN_DIR = Path(__file__).parent / "golden"


def get_golden_tests():
    """Discover all .silk files with matching .expected files."""
    tests = []
    for silk_file in GOLDEN_DIR.glob("*.silk"):
        expected_file = silk_file.with_suffix(".expected")
        if expected_file.exists():
            tests.append((silk_file.stem, silk_file, expected_file))
    return tests


@pytest.mark.parametrize("name,silk_file,expected_file", get_golden_tests())
def test_golden(name, silk_file, expected_file):
    """Run silk file and compare output to expected."""
    source = silk_file.read_text()
    expected = expected_file.read_text().strip()

    interp = Interpreter()
    interp.run(source)

    actual = "\n".join(interp.output_lines).strip()
    assert actual == expected, f"Golden test '{name}' failed:\nExpected:\n{expected}\n\nActual:\n{actual}"
