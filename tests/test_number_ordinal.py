"""
Tests for number .toOrdinal() method.
"""

from silk.interpreter import Interpreter


class TestNumberOrdinal:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_ordinal_1(self):
        output = self._run('print(1.toOrdinal())')
        assert output[-1] == "1st"

    def test_ordinal_2(self):
        output = self._run('print(2.toOrdinal())')
        assert output[-1] == "2nd"

    def test_ordinal_3(self):
        output = self._run('print(3.toOrdinal())')
        assert output[-1] == "3rd"

    def test_ordinal_11(self):
        output = self._run('print(11.toOrdinal())')
        assert output[-1] == "11th"

    def test_ordinal_21(self):
        output = self._run('print(21.toOrdinal())')
        assert output[-1] == "21st"

    def test_ordinal_112(self):
        output = self._run('print(112.toOrdinal())')
        assert output[-1] == "112th"
