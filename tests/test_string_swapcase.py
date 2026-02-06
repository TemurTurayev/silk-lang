"""
Tests for string .swapCase() method.
"""

from silk.interpreter import Interpreter


class TestStringSwapCase:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_swapCase_basic(self):
        output = self._run('''
print("Hello World".swapCase())
''')
        assert output[-1] == "hELLO wORLD"

    def test_swapCase_all_lower(self):
        output = self._run('''
print("abc".swapCase())
''')
        assert output[-1] == "ABC"

    def test_swapCase_all_upper(self):
        output = self._run('''
print("XYZ".swapCase())
''')
        assert output[-1] == "xyz"
