"""
Tests for number .digitAllDistinct() method - check if all digits are unique.
"""

from silk.interpreter import Interpreter


class TestNumberDigitAllDistinct:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitAllDistinct_true(self):
        output = self._run('print(1234.digitAllDistinct())')
        assert output[-1] == "true"

    def test_digitAllDistinct_false(self):
        output = self._run('print(1224.digitAllDistinct())')
        assert output[-1] == "false"
