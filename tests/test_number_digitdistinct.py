"""
Tests for number .digitDistinct() method - count of unique digits.
"""

from silk.interpreter import Interpreter


class TestNumberDigitDistinct:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_digitDistinct_basic(self):
        output = self._run('print(112233.digitDistinct())')
        assert output[-1] == "3"

    def test_digitDistinct_all_unique(self):
        output = self._run('print(1234.digitDistinct())')
        assert output[-1] == "4"
