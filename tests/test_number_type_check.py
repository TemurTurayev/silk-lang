"""
Tests for number .isInteger() and .isFloat() methods.
"""

from silk.interpreter import Interpreter


class TestNumberTypeCheck:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_isInteger_int(self):
        output = self._run('''
print(42.isInteger())
''')
        assert output[-1] == "true"

    def test_isInteger_float(self):
        output = self._run('''
print(3.14.isInteger())
''')
        assert output[-1] == "false"

    def test_isFloat_float(self):
        output = self._run('''
print(3.14.isFloat())
''')
        assert output[-1] == "true"

    def test_isFloat_int(self):
        output = self._run('''
print(42.isFloat())
''')
        assert output[-1] == "false"
