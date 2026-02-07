"""
Tests for string .extractEmails() method.
"""

from silk.interpreter import Interpreter


class TestStringExtractEmails:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_extractEmails_basic(self):
        output = self._run('print("contact us at foo@bar.com or hi@test.org".extractEmails())')
        assert output[-1] == "[foo@bar.com, hi@test.org]"

    def test_extractEmails_none(self):
        output = self._run('print("no emails here".extractEmails())')
        assert output[-1] == "[]"

    def test_extractEmails_single(self):
        output = self._run('print("email: user@example.com".extractEmails())')
        assert output[-1] == "[user@example.com]"
