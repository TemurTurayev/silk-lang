"""
Tests for Array.filled() builtin function.
"""

from silk.interpreter import Interpreter


class TestArrayFilled:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_filled_basic(self):
        output = self._run('''
print(Array.filled(3, 0))
''')
        assert output[-1] == "[0, 0, 0]"

    def test_filled_string(self):
        output = self._run('''
print(Array.filled(2, "hi"))
''')
        assert output[-1] == "[hi, hi]"

    def test_filled_empty(self):
        output = self._run('''
print(Array.filled(0, 1))
''')
        assert output[-1] == "[]"
