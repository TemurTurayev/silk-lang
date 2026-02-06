"""
Tests for number .toBase(base) method.
"""

from silk.interpreter import Interpreter


class TestNumberToBase:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toBase_binary(self):
        output = self._run('print(10.toBase(2))')
        assert output[-1] == "1010"

    def test_toBase_octal(self):
        output = self._run('print(255.toBase(8))')
        assert output[-1] == "377"

    def test_toBase_hex(self):
        output = self._run('print(255.toBase(16))')
        assert output[-1] == "ff"

    def test_toBase_36(self):
        output = self._run('print(35.toBase(36))')
        assert output[-1] == "z"
