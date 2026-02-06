"""
Tests for string .isBlank() method.
"""

from silk.interpreter import Interpreter


class TestStringBlank:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_isBlank_empty(self):
        output = self._run('''
print("".isBlank())
''')
        assert output[-1] == "true"

    def test_isBlank_spaces(self):
        output = self._run('''
print("   ".isBlank())
''')
        assert output[-1] == "true"

    def test_isBlank_text(self):
        output = self._run('''
print("hello".isBlank())
''')
        assert output[-1] == "false"

    def test_isBlank_mixed(self):
        output = self._run('''
print(" a ".isBlank())
''')
        assert output[-1] == "false"
