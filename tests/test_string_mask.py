"""
Tests for string .mask() method (medical data privacy).
"""

from silk.interpreter import Interpreter


class TestStringMask:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mask_basic(self):
        output = self._run('''
print("1234567890".mask("*", 4))
''')
        assert output[-1] == "******7890"

    def test_mask_email(self):
        output = self._run('''
print("john@example.com".mask("*", 4))
''')
        assert output[-1] == "************.com"

    def test_mask_short(self):
        output = self._run('''
print("abc".mask("*", 5))
''')
        assert output[-1] == "abc"

    def test_mask_ssn(self):
        output = self._run('''
print("123-45-6789".mask("X", 4))
''')
        assert output[-1] == "XXXXXXX6789"
