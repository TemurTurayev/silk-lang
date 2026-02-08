"""
Tests for number .digitMirror() method - concat number with its digit reverse.
"""

from silk.interpreter import Interpreter


class TestNumberDigitMirror:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitMirror_123(self):
        output = self._run('print(123.digitMirror())')
        assert output[-1] == "123321"

    def test_digitMirror_45(self):
        output = self._run('print(45.digitMirror())')
        assert output[-1] == "4554"
