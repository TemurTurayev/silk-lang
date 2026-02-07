"""
Tests for string .isPhoneNumber() method.
"""

from silk.interpreter import Interpreter


class TestStringIsPhoneNumber:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_isPhoneNumber_valid(self):
        output = self._run('print("+1-555-123-4567".isPhoneNumber())')
        assert output[-1] == "true"

    def test_isPhoneNumber_simple(self):
        output = self._run('print("5551234567".isPhoneNumber())')
        assert output[-1] == "true"

    def test_isPhoneNumber_invalid(self):
        output = self._run('print("hello".isPhoneNumber())')
        assert output[-1] == "false"
