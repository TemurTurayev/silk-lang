"""
Tests for string .isEmail() basic email validation.
"""

from silk.interpreter import Interpreter


class TestStringIsEmail:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_isEmail_valid(self):
        output = self._run('print("user@example.com".isEmail())')
        assert output[-1] == "true"

    def test_isEmail_invalid_no_at(self):
        output = self._run('print("userexample.com".isEmail())')
        assert output[-1] == "false"

    def test_isEmail_invalid_no_dot(self):
        output = self._run('print("user@example".isEmail())')
        assert output[-1] == "false"

    def test_isEmail_empty(self):
        output = self._run('print("".isEmail())')
        assert output[-1] == "false"
