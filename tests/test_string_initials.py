"""
Tests for string .initials() method.
"""

from silk.interpreter import Interpreter


class TestStringInitials:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_initials_basic(self):
        output = self._run('print("John Doe".initials())')
        assert output[-1] == "JD"

    def test_initials_three(self):
        output = self._run('print("Martin Luther King".initials())')
        assert output[-1] == "MLK"

    def test_initials_single(self):
        output = self._run('print("Alice".initials())')
        assert output[-1] == "A"
