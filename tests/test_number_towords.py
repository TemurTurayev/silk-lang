"""
Tests for number .toWords() method.
"""

from silk.interpreter import Interpreter


class TestNumberToWords:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toWords_zero(self):
        output = self._run('print(0.toWords())')
        assert output[-1] == "zero"

    def test_toWords_small(self):
        output = self._run('print(42.toWords())')
        assert output[-1] == "forty-two"

    def test_toWords_hundred(self):
        output = self._run('print(100.toWords())')
        assert output[-1] == "one hundred"

    def test_toWords_complex(self):
        output = self._run('print(215.toWords())')
        assert output[-1] == "two hundred fifteen"
