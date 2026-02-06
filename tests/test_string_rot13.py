"""
Tests for string .rot13() method.
"""

from silk.interpreter import Interpreter


class TestStringRot13:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_rot13_basic(self):
        output = self._run('print("Hello".rot13())')
        assert output[-1] == "Uryyb"

    def test_rot13_roundtrip(self):
        output = self._run('print("Hello".rot13().rot13())')
        assert output[-1] == "Hello"

    def test_rot13_preserves_non_alpha(self):
        output = self._run('print("Hello, World! 123".rot13())')
        assert output[-1] == "Uryyb, Jbeyq! 123"
