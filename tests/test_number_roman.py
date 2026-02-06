"""
Tests for number .toRoman() method.
"""

from silk.interpreter import Interpreter


class TestNumberToRoman:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toRoman_1(self):
        output = self._run('print(1.toRoman())')
        assert output[-1] == "I"

    def test_toRoman_4(self):
        output = self._run('print(4.toRoman())')
        assert output[-1] == "IV"

    def test_toRoman_9(self):
        output = self._run('print(9.toRoman())')
        assert output[-1] == "IX"

    def test_toRoman_42(self):
        output = self._run('print(42.toRoman())')
        assert output[-1] == "XLII"

    def test_toRoman_2024(self):
        output = self._run('print(2024.toRoman())')
        assert output[-1] == "MMXXIV"
