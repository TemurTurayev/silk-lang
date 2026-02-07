"""
Tests for string .isDate() method - checks YYYY-MM-DD format.
"""

from silk.interpreter import Interpreter


class TestStringIsDate:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_isDate_valid(self):
        output = self._run('print("2024-01-15".isDate())')
        assert output[-1] == "true"

    def test_isDate_invalid(self):
        output = self._run('print("not-a-date".isDate())')
        assert output[-1] == "false"

    def test_isDate_wrong_format(self):
        output = self._run('print("01/15/2024".isDate())')
        assert output[-1] == "false"
